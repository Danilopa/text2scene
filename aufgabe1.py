import spacy
import xml.etree.ElementTree as ET
data_files = ["/Users/danilopantic/Desktop/Traning/RFC/Bicycles.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Amazon.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Andes.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Argentina.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Bogota.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Cartagena.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Colon.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Copala.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Cusco.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Durango.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Floods.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Glaciers.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Guatemala.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/GuerreroNegro.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Hollywood.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/HorseAssisted.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Huaraz.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Hurricanes.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/IntoTheAndes.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/LaPaz.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Loreto.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/LosAngeles.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/MachuPicho.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Manaus.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Mazatlan.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/MexicoCity.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Monarchs.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Oceans.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Paramo.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Peru.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/BuenosAires.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Ensenada.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Honduras.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Lima.xml",
              "/Users/danilopantic/Desktop/Traning/RFC/Medellin.xml",
              "/Users/danilopantic/Desktop/Traning/CP/45_N_22_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/45_N_23_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_21_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_22_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_23_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_24_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_25_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_26_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_27_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/46_N_28_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_22_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_23_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_24_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_25_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_26_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_27_E.xml",
              "/Users/danilopantic/Desktop/Traning/CP/47_N_28_E.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToMadrid/Bourbon_Madrid.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToMadrid/Highlights_of_the_Prado_Museum.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToMadrid/Modern_Madrid.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToMadrid/Museo_del_Prado.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToMadrid/Near_the_Puerta_del_Sol.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToJapan/Asakusa.xml",
              "/Users/danilopantic/Desktop/Traning/ANC/WhereToJapan/Ginza.xml"]

nlp = spacy.load("en_core_web_sm")

ADJ = 0
ADV = 0
INTJ = 0
NOUN = 0
PROPN = 0
VERB = 0
ADP = 0
AUX = 0
CONJ = 0
DET = 0
NUM = 0
PART = 0
PRON = 0
SCONJ = 0
PUNCT = 0
SYM = 0
X = 0

for x in data_files:
    tree = ET.parse(x)
    root = tree.getroot()
    doc = nlp(root[0].text)

    for token in doc:
        if token.pos_ == "ADJ":
            ADJ = ADJ + 1
        elif token.pos_ == "ADV":
            ADV = ADV + 1
        elif token.pos_ == "INTJ":
            INTJ = INTJ + 1
        elif token.pos_ == "NOUN":
            NOUN = NOUN + 1
        elif token.pos_ == "PROPN":
            PROPN = PROPN + 1
        elif token.pos_ == "VERB":
            VERB = VERB + 1
        elif token.pos_ == "ADP":
            ADP = ADP + 1
        elif token.pos_ == "AUX":
            AUX = AUX + 1
        elif token.pos_ == "CONJ":
            CONJ = CONJ + 1
        elif token.pos_ == "DET":
            DET = DET + 1
        elif token.pos_ == "NUM":
            NUM = NUM + 1
        elif token.pos_ == "PART":
            PART = PART + 1
        elif token.pos_ == "PRON":
            PRON = PRON + 1
        elif token.pos_ == "SCONJ":
            SCONJ = SCONJ + 1
        elif token.pos_ == "PUNCT":
            PUNCT = PUNCT + 1
        elif token.pos_ == "SYM":
            SYM = SYM + 1
        elif token.pos_ == "X":
            X = X + 1

print("ADJ:", ADJ)
print("ADV:", ADV)
print("INTJ", INTJ)
print("NOUN", NOUN)
print("PROPN", PROPN)
print("VERB", VERB)
print("ADP", ADP)
print("AUX",AUX)
print("COUJ", CONJ)
print("DET", DET)
print("NUM", NUM)
print("PART", PART)
print("PRON", PRON)
print("SCONJ", SCONJ)
print("PUNCT", PUNCT)
print("SYM", SYM)
print("X", X)