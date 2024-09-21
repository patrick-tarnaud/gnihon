import os
from gnihon.xml.jmdict import load_jmdict, Entry, K_ele, R_ele
from pprint import pprint

def clean_str(str: str) -> str:
    return str.replace('\n', '').replace(' ', '')

def test_jmdict():
    entries: list[Entry] = load_jmdict(os.getcwd() + '/tests/resources/JMdict.xml')

    assert len(entries) == 5
    

    # <entry>
    #     <ent_seq>1260110</ent_seq>
    #     <k_ele>
    #         <keb>見本市</keb>
    #         <ke_pri>news1</ke_pri>
    #         <ke_pri>nf17</ke_pri>
    #     </k_ele>
    #     <r_ele>
    #         <reb>みほんいち</reb>
    #         <re_pri>news1</re_pri>
    #         <re_pri>nf17</re_pri>
    #     </r_ele>
    #     <sense>
    #         <pos>&n;</pos>
    #         <gloss>trade fair</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="dut">handelsbeurs</gloss>
    #         <gloss xml:lang="dut">vakbeurs</gloss>
    #         <gloss xml:lang="dut">{gew.} foor</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="ger">Messe</gloss>
    #         <gloss xml:lang="ger">Mustermesse</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="hun">termékbemutató</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="rus">торговля [на ярмарке] по образцам; выставка образцов (для
    #             продажи); выставка-продажа (товаров, изделий)</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="spa">feria de muestras</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="swe">fackmässa</gloss>
    #     </sense>
    # </entry>
    current = entries[0]
    current_str ="""
        Entry(
            ent_seq=1260110, 
            k_ele=[
                K_ele(
                    keb='見本市', 
                    ke_inf=[], 
                    ke_pri=['news1', 'nf17']
                )], 
            r_ele=[
                R_ele(
                    reb='みほんいち',
                    re_nokanji='',
                    re_restr=[],
                    re_inf=[],
                    re_pri=['news1','nf17']
                )], 
            sense=[
                Sense(
                    pos='&n;',
                    gloss='trade fair'
                )
            ]
            )
    """
    pprint(current)
    # assert clean_str(str(current)) == clean_str(current_str) 


    assert entries[1].ent_seq == 1260120
    assert entries[2].ent_seq == 1260130
    assert entries[3].ent_seq == 1260140
    assert entries[4].ent_seq == 1260150

