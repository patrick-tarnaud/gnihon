import os
from gnihon.xml.jmdict import Entry, load_jmdict

def main() -> None:
    # print(os.getcwd())
    entries: list[Entry] = load_jmdict(os.getcwd() + "/gnihon/resources/JMdict")
    print(len(entries))
    print(entries[100])
    print(entries[1000])
