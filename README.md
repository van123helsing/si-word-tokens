# si-word-tokens
Orodje, ki generira seznam najbolj pogostih lem v slovenskem jeziku na podlagi [Morphological lexicon Sloleks 3.0](https://www.clarin.si/repository/xmlui/handle/11356/1745).
Seznam se generira v TXT format, kjer vsaka vrstica predstavlja eno lemo in je urejen od najbolj do najmanj pogostih pojavitvah v Gigafida.

Generiran seznam lem je posebej koristen za uporabo v drugih orodjih, kot je na primer [wordninja](https://github.com/keredson/wordninja), katerega glavni namen je razdeliti stavek brez presledkov na smiselne besede.

Primer stavka:
```angular2html
Osnovninamenportalajeponuditiupravnestoritveuporabnikomprekosvetovnegaspletaintakopolegklasičnihzagotovitidodatno,elektronskopotzaopravljanjetehstoritev.Kerbiradizagotoviliodličnouporabniškoizkušnjo,jeportalzasnovanvskladussodobnimitehnološkimiinoblikovalskimismernicamiinusmerjenkuporabnikom.
```

Primer uporabe:

```python
import wordninja

# Input sentence
sentence = "Osnovninamenportalajeponuditiupravnestoritveuporabnikomprekosvetovnegaspletaintakopolegklasičnihzagotovitidodatno,elektronskopotzaopravljanjetehstoritev.Kerbiradizagotoviliodličnouporabniškoizkušnjo,jeportalzasnovanvskladussodobnimitehnološkimiinoblikovalskimismernicamiinusmerjenkuporabnikom."

lm = wordninja.LanguageModel('output.txt.gz')
reconstructed_sentence = " ".join(lm.split(sentence))


print(reconstructed_sentence)

```
> OPOMBA:
> 
> **wordninja** privzeto ne podpira šumnikov. Če želimo to podpreti je potrebno spremeniti 81. vrstico v datoteki **wordninja.py** sledeče:
> 
> _SPLIT_RE = re.compile("[^a-zA-Z0-9'čšžćđČŠŽĆĐ]+")

Rezultat po obdelavi stavka z orodjem "wordninja" in našim modelom::
```
Osnovni namen portala je ponuditi upravne storitve uporabnikom preko svetovnega spleta in tako poleg klasičnih zagotoviti dodatno elektronsko pot za opravljanje teh storitev Ker bi radi zagotovili odlično uporabniško izkušnjo je portal zasnovan v skladu s sodobnimi tehnološkimi in oblikovalskimi smernicami in usmerjen k uporabnikom
```