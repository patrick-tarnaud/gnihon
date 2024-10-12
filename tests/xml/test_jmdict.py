import os
from gnihon.xml.jmdict import load_jmdict, Entry
import pytest
from pprint import pprint  # noqa: F401

NB_ENTRIES = 3

template: str = """
Entry(
    ent_seq='', 
    k_ele=[
        K_ele(
            keb='', 
            ke_inf=[], 
            ke_pri=[]
        )], 
    r_ele=[
        R_ele(
            reb='',
            re_nokanji='',
            re_restr=[],
            re_inf=[],
            re_pri=[]
        )], 
    sense=[
        Sense(
            stagk=[],
            stagr=[],
            pos=[],
            xref=[],
            ant=[],
            field=[],
            misc=[],
            s_inf=[],
            lsource=[
            	Source(
        		lang='',
        		ls_type='',
        		ls_wasei=False,
        		text=''
            	)
            ],
            dial=[],
            gloss=[
            	Gloss(
            		gloss='',
            		lang='',
            		g_type=''
            		)
            	]
        )
    ]
)
"""


def clean_str(str: str) -> str:
    return str.replace("\n", "").replace(" ", "").replace('\r', '')


@pytest.fixture
def entries() -> list[Entry]:
    entries = load_jmdict(os.getcwd() + "/tests/resources/JMdict.xml")
    assert len(entries) == NB_ENTRIES
    return entries


def test_1(entries: list[Entry]) -> None:
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
    current_str = """
        Entry(
            ent_seq='1260110', 
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
                    stagk=[],
                    stagr=[],
                    pos=['noun (common) (futsuumeishi)'],
                    xref=[],
                    ant=[],
                    field=[],
                    misc=[],
                    s_inf=[],
                    lsource=[],
                    dial=[],
                    gloss=[Gloss(gloss='trade fair',lang='eng',g_type='')]
                )
            ]
            )
    """
    assert clean_str(str(current)) == clean_str(current_str)
    # print('Entry loaded')
    # pprint(clean_str(str(current)))
    # print('Entry reference')
    # pprint(clean_str(current_str))


def test_2(entries: list[Entry]) -> None:
    #  <entry>
    #     <ent_seq>1053260</ent_seq>
    #     <r_ele>
    #         <reb>コンビナートキャンペーン</reb>
    #     </r_ele>
    #     <r_ele>
    #         <reb>コンビナート・キャンペーン</reb>
    #     </r_ele>
    #     <sense>
    #         <pos>&n;</pos>
    #         <misc>&obs;</misc>
    #         <lsource xml:lang="rus">kombinat</lsource>
    #         <lsource xml:lang="eng" ls_type="part" ls_wasei="y">campaign</lsource>
    #         <gloss>coordinated advertising campaign for various different products (sharing brand
    #             name, slogans, etc.)</gloss>
    #     </sense>
    #     <sense>
    #         <gloss xml:lang="ger">industrieübergreifende Werbekampagne</gloss>
    #     </sense>
    # </entry>

    current = entries[1]
    current_str = """
        Entry(
            ent_seq='1053260', 
            k_ele=[], 
            r_ele=[
                R_ele(
                    reb='コンビナートキャンペーン',
                    re_nokanji='',
                    re_restr=[],
                    re_inf=[],
                    re_pri=[]
                ),
                R_ele(
                    reb='コンビナート・キャンペーン',
                    re_nokanji='',
                    re_restr=[],
                    re_inf=[],
                    re_pri=[]
                )], 
            sense=[
                Sense(
                    stagk=[],
                    stagr=[],
                    pos=['noun (common) (futsuumeishi)'],
                    xref=[],
                    ant=[],
                    field=[],
                    misc=['obsolete term'],
                    s_inf=[],
                    lsource=[
                        Source(
                            lang='rus',
                            ls_type='',
                            ls_wasei=False,
                            text='kombinat'
                        ),
                        Source(
                            lang='eng',
                            ls_type='part',
                            ls_wasei=True,
                            text='campaign'
                        )
                    ],
                    dial=[],
                    gloss=[
                        Gloss(
                            gloss='coordinated advertising campaign for various different products (sharing brand name, slogans, etc.)',
                            lang='eng',
                            g_type=''
                            )
                        ]
                )                
            ]
        )
   """
    assert clean_str(str(current)) == clean_str(current_str)