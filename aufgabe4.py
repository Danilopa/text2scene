import spacy
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

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

li =[]
for x in data_files:
    tree = ET.parse(x)
    root = tree.getroot()
    doc = nlp(root[0].text)


    for sent in doc.sents:
        x = sent.text
        y = x.replace(" ", "")
        z = len(x) - len(y)
        li.append(z + 1)

li.sort()
print("1",li)

array_x = []
array_y = []
x = 0
while x < len(li):
    if li[x] not in array_x:
        a = li[x]
        array_x.append(a)
        array_y.append(len(list(filter(lambda z: z == a, li))))
    x = x + 1

plt.bar(array_x,array_y)
plt.xlabel("Satzlänge")
plt.ylabel("Häufigkeit")
plt.show()
