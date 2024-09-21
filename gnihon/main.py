import xml.etree.ElementTree as ET
import os

class Entry:
    seq: str

def main() -> None:
    print(os.getcwd())
    tree = ET.parse(os.getcwd() + '/gnihon/data/JMdict')
    root = tree.getroot()
    i = 0
    for entry in root:
        print(entry.find('ent_seq').text) # type: ignore
        i+=1
        if i == 10:
            break
