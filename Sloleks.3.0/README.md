The Sloleks Morphological Lexicon of Slovene
v3.0
http://hdl.handle.net/11356/1745
Authors: Čibej, Jaka; Gantar, Kaja; Dobrovoljc, Kaja; Krek, Simon; Holozan, Peter; Erjavec, Tomaž; Romih, Miro; Arhar Holdt, Špela; Krsnik, Luka; Robnik-Šikonja, Marko

Sloleks is a reference morphological lexicon of Slovene that was developed to be used in various NLP applications and language manuals. It contains Slovene lemmas, their inflected or derivative word forms and the corresponding grammatical description. In addition to the approx. 100,000 entries already available in Sloleks 2.0 (http://hdl.handle.net/11356/1230), Sloleks 3.0 contains an additional cca. 265,000 newly generated entries from the most frequent lemmas in Gigafida 2.0 (http://hdl.handle.net/11356/1320) not yet included in previous versions of Sloleks. For verbs, adjectives, adverbs, and common nouns, the lemmas were checked manually by three annotators and included in Sloleks only if confirmed as legitimate by at least one annotator. No manual checking was performed on proper nouns.

Lemmatization rules, part-of-speech categorization and the set of feature-value pairs follow the JOS morphosyntactic specifications. In addition to grammatical information, each word form is also given the information on its absolute corpus frequency and its compliance with the reference language standard. In addition, most entries contain information on their morphological patterns (see http://hdl.handle.net/11356/1411 for more on morphological patterns).

Similarly to Sloleks 2.0, version 3.0 includes accentuated word forms automatically generated through neural networks (Krsnik 2017). For the 100,000 entries from Sloleks 2.0, the accentuated forms were manually corrected, whereas the accentuated forms for the other 265,000 entries are fully automatic. IPA and SAMPA phonetic transcriptions were generated automatically using an improved G2P system for Slovene developed within the RSDO project (see https://github.com/clarinsi/slovene_g2p).

Version 3.0 is encoded in XML, but unlike 2.0, which used the LMF format, the new version uses a custom XML format developed for the morphological lexicon by the Centre for Language Resources and Technologies of the University of Ljubljana (see the included .xsd files and below for details).

Reference:
Krsnik, Luka. Napovedovanje naglasa slovenskih besed z metodami strojnega učenja: magistrsko delo: magistrski program druge stopnje Računalništvo in informatika. Ljubljana: [L. Krsnik], 2017. http://eprints.fri.uni-lj.si/3978/

#### ENTRY STATUS ####
Entries in Sloleks 3.0 are annotated as either MANUAL or AUTOMATIC. Manual entries are the entries already available in Sloleks 2.0 - their accentuated forms were manually corrected within the RSDO project. Automatic entries were generated entirely automatically.
XML Example: <lexicon><entry><head><status>MANUAL</status>...
XPath: /lexicon/entry/head/status


#### LEMMA ####
The lemma of each entry is provided in the <head> of each <entry>.
XML Example: <lexicon><entry><head><headword><lemma>miza</lemma></headword>...
XPath: /lexicon/entry/head/headword/lemma

#### SLOLEKS ID AND SLOLEKS KEY ####
The entry ID and key are provided under the <lexicalUnit> tag as separate attributes. The ID is an MD5 hash of the Sloleks key.
XML Example: <lexicon><entry><head><lexicalUnit sloleksId="LE_dcc15ec9b2fb16363c330cb4b550b2a8" sloleksKey="S_vojskovodja" type="single">...
XPath: /lexicon/entry/head/lexicalUnit

#### PART-OF-SPEECH CATEGORY ####
The part-of-speech category (e.g. noun, verb, adverb, adjective, ...) of each entry is listed under <grammar>.
XML Example: <lexicon><entry><head><grammar><category>noun</category>...
XPath: /lexicon/entry/head/grammar/category

#### PRONUNCIATION TYPE ####
Pronunciation type is available only for the approx. 100,800 entries from Sloleks 2.0. Its possible values are the following:
* Slovene G2P -> the word follows Slovene grapheme-to-phoneme conversion rules;
* Slovene G2P with minor deviation -> the word follows Slovene grapheme-to-phoneme conversion rules (with a slight deviation, e.g. if the grapheme "s" is pronounced as "z" (e.g. "visažistka"), which is unusual.
* Other G2P -> the word does not follow Slovene grapheme-to-phoneme conversion rules (e.g. "Shakespeare")
* Ambiguous G2P -> the word can be pronounced either as a Slovene G2P word or as an Other G2P word (e.g. "Amanda")
* Acronym -> the word is pronounced as an acronym (e.g. "FBI", "RTV")
* Abbreviation -> the word is an abbreviation of a different word (e.g. "ga." - "gospa")
* Numeral -> the word is a cardinal number (e.g. "500", "XVI")
* Symbol -> the word is a symbol (e.g. "mlrd", "kg")

TAKE NOTE: Acronyms, abbreviations, numerals, and symbols have no pronunciations in version 3.0.

XML Example: <lexicon><entry><head><grammar><subcategory type="pronunciation">Slovene G2P</subcategory>...
XPath: /lexicon/entry/head/grammar/subcategory[@type="pronunciation"]

#### LEXEME-LEVEL GRAMMAR FEATURES ####
Grammatical features (aside from part-of-speech, which is listed separately in <category>; see above) that are inherent to the lemma and not dependent on form - e.g. common/proper for nouns, perfective/progressive/biaspectual for verbs - are listed under <grammar> as <grammarFeature>.

XML Example: <lexicon><entry><head><grammar><grammarFeature name="type">common</grammarFeature>...
XPath: /lexicon/entry/head/grammar/grammarFeature

#### LEMMA FREQUENCY ####
The frequency of the lemma (or, more accurately, the lemma in combination with its lexeme-level features; e.g. "miza" as a common feminine noun) from the Gigafida 2.0 corpus are listed as <measure> under <measureList>.

XML Example: <lexicon><entry><head><measureList><measure type="frequency" source="Gigafida 2.0">91</measure>...
XPath: /lexicon/entry/head/measureList/measure[@type="frequency"]

#### RELATED ENTRIES ####
Entries that are morphologically related to the current entry are listed as <relatedEntry> in <relatedEntryList>. In Sloleks 3.0, related entries are only available for entries with <status>MANUAL</status>. Each <relatedEntry> is also listed with an "origin" attribute, which contains the Sloleks ID of the related entry.

XML Example: <lexicon><entry><head><relatedEntryList><relatedEntry origin="LE_b41cefb0420209c6ce3102fc4940f7ac">miza</relatedEntry>...
XPath: /lexicon/entry/head/relatedEntryList/relatedEntry

#### MORPHOSYNTACTIC TAGS ####
Morphosyntactic tags are available for each word form. In version 3.0, they are listed in Slovene according to the Multext-East v6 system.

XML Example: <lexicon><entry><body><wordFormList><wordForm><msd language="sl" system="JOS">Sozei</msd>...
XPath: /lexicon/entry/body/wordFormList/wordForm/msd

#### FORM-LEVEL GRAMMAR FEATURES ####
Grammar features dependent on the form (e.g. number and case for nouns) are listed similarly to lexeme-level grammar features (see above).

XML Example: <lexicon><entry><body><wordFormList><wordForm><grammarFeatureList><grammarFeature name="number">singular</grammarFeature>...
XPath: /lexicon/entry/body/wordFormList/wordForm/grammarFeatureList/grammarFeature

#### FORM REPRESENTATIONS ####
All possible representations of the word form (e.g. the genitive forms for "vojskovodja": "vojskovodja" and "vojskovodje", are both listed under the same word form as two separate form representations.

In version 3.0, the formRepresentations list contains orthographical forms (<orthography>), dynamic accentuation forms (<accentuation>), and pronunciation forms (<pronunciation>).

For orthographical forms, their frequencies from Gigafida 2.0 are also provided under <measure type="frequency" source="Gigafida 2.0">. Morphological patterns are also provided for most entries.

XML Example: <lexicon><body><wordFormList><wordForm><formRepresentations><orthographyList><orthography morphologyPatterns="Sm7.2.o"><form>vojskovodja</form><measureList><measure type="frequency" source="Gigafida 2.0">1019</measure>...
XPath (orthographical form): lexicon/entry/body/wordFormList/wordForm/formRepresentations/orthographyList/orthography/form
XPath (morphological pattern): lexicon/entry/body/wordFormList/wordForm/formRepresentations/orthographyList/orthography[@morphologyPatterns]
XPath (orthographical form frequency): lexicon/entry/body/wordFormList/wordForm/formRepresentations/orthographyList/measureList/measure

If dynamic accentuated forms are provided, they are listed under <accentuationList type="dynamic">:

XML Example: <lexicon><entry><body><wordFormList><wordForm><formRepresentations><accentuationList type="dynamic"><accentuation><form>vojskovódja</form>...
XPath: lexicon/entry/body/wordFormList/wordForm/form/formRepresentations/accentuationList[@type="dynamic"]/accentuation/form

Pronunciation forms (either in IPA or SAMPA) are provided under <pronunciationList>:

XML Example: <lexicon><entry><body><wordFormList><wordForm><formRepresentations><pronunciationList><pronunciation><form script="IPA">ʋɔɪskɔˈʋoːdja</form><form script="SAMPA">vOIskO"vo:dja</form></pronunciation>...
XPath (IPA): /lexicon/entry/body/wordFormList/wordForm/form/formRepresentations/pronunciationList/pronunciation/form[@script="IPA"]
XPath (SAMPA): /lexicon/entry/body/wordFormList/wordForm/form/formRepresentations/pronunciationList/pronunciation/form[@script="SAMPA"]

#### ACKNOWLEDGMENTS ####
Ministry of Education, Science and Sport 3311-08-986003 "Communication in Slovene"
Jožef Stefan Institute CLARIN "CLARIN.SI"
ARRS (Slovenian Research Agency) P6-0411 "Language Resources and Technologies for Slovene"
Ministry of Culture C3340-20-278001 "Development of Slovene in a Digital Environment"




