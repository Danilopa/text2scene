import spacy
import networkx as nx
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

datafile = "/Users/danilopantic/Desktop/Traning/RFC/Bicycles.xml"

nlp = spacy.load("en_core_web_sm")

tree = ET.parse(datafile)
root = tree.getroot()

text = root[0].text
doc = nlp(text)


G = nx.Graph()


for x in root[1]:
     if x.tag == "PLACE":
          G.add_node(x.attrib['text'])

nx.draw(G, node_color='w', with_labels=True)

for x in root[1]:
     if x.tag == "LOCATION":
          G.add_node(x.attrib['text'])

nx.draw(G, node_color='y', with_labels=True)


for x in root[1]:
     if x.tag == "SPATIAL_ENTITY":
          G.add_node(x.attrib['text'])

nx.draw(G, node_color='g', with_labels=True)


for x in root[1]:
     if x.tag == "NONMOTIONEVENT":
          G.add_node(x.attrib['text'])

nx.draw(G, node_color='r', with_labels=True)


for x in root[1]:
     if x.tag == "PATH":
          G.add_node(x.attrib['text'])

nx.draw(G, node_color='b', with_labels=True)
plt.show()