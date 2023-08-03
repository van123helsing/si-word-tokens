from lxml import etree
from collections import OrderedDict

# Create a dictionary to store unique headwords and forms
words = OrderedDict()


def parse_xml(xml_file):
    # Parse the XML file using the provided XSD schemas
    parser = etree.XMLParser(
        schema=etree.XMLSchema(etree.parse("Sloleks.3.0/xml_schemas/morphological_lexicon.xsd")),
    )
    tree = etree.parse(xml_file, parser)

    # Extract "headword" elements
    for entry in tree.xpath("/lexicon/entry"):
        headword = entry.findtext("head/headword/lemma")
        frequency = int(entry.findtext("head/measureList/measure"))
        if frequency > 100 and headword not in words:
            words[headword] = frequency

    # Extract "form" elements
    for orthography in tree.xpath("/lexicon/entry/body/wordFormList/wordForm/formRepresentations/orthographyList/orthography"):
        form = orthography.findtext("form")
        frequency = int(orthography.findtext("measureList/measure"))
        if frequency > 100 and form not in words:
            words[form] = frequency


if __name__ == "__main__":
    # The number of input files
    num_files = 102

    # Process each input file and write the results to the output file
    for i in range(1, num_files + 1):
        input_filename = f"Sloleks.3.0/sloleks_3.0_{i:03d}.xml"
        parse_xml(input_filename)
        print(i)

    # sort words by occurrences (more frequent first)
    sorted_words = sorted(words.items(), key=lambda item: item[1], reverse=True)
    with open("output.txt", 'w', encoding='utf-8') as output_file:
        output_file.write("")
        for word in sorted_words:
            output_file.write(word[0] + '\n')

