from dataclasses import dataclass
import xml.etree.ElementTree as ET


class JMdictParseError(Exception):
    def __init__(self, mother_tag: str, child_tag: str) -> None:
        super().__init__(f'Erreur lors du parsing XML de JMdict. Dans {mother_tag}, la balise {child_tag} est inconnue.')

@dataclass
class K_ele:
    keb: str
    ke_inf: list[str]
    ke_pri: list[str]

@dataclass
class R_ele:
    reb: str
    re_nokanji: str | None
    re_restr: list[str]
    re_inf: list[str]
    re_pri: list[str]

@dataclass
class Source:
    lang: str
    ls_type: str
    ls_wasei: str
    text: str

@dataclass
class Gloss:
    gloss: str
    lang: str
    g_type: str    

@dataclass
class Sense:
    stagk: list[str]
    stagr: list[str]
    pos: list[str]
    xref: list[str] 
    ant: list[str]
    field: list[str]
    misc: list[str]
    s_inf: list[str]
    lsource: list[Source]
    dial: list[str]
    gloss: list[Gloss]

    
@dataclass
class Entry:
    ent_seq: int
    k_ele: list[K_ele]
    r_ele: list[R_ele]
    sense: list[Sense]


def parse_sense(element: ET.Element) -> Sense | None:

    def parse_lsource(element: ET.Element) -> Source | None:
        return None

    def parse_gloss(element: ET.Element) -> Gloss | None:
        return None

    stagk: list[str] = []
    stagr: list[str] = []
    pos: list[str] = []
    xref: list[str] = []
    ant: list[str] = []
    field: list[str] = []
    misc: list[str] = []
    s_inf: list[str] = []
    lsource: list[Source] = []
    dial: list[str] = []
    gloss: list[Gloss] = []

    for child in element:
        match child.tag:
            case 'stagk':
                stagk.append(child.text or '')
            case 'stagr':
                stagr.append(child.text or '')
            case 'pos':
                pos.append(child.text or '')
            case 'xref':     
                xref.append(child.text or '')           
            case 'ant':
                ant.append(child.text or '')
            case 'field':
                field.append(child.text or '')
            case 'misc':
                misc.append(child.text or '')
            case 's_inf':
                s_inf.append(child.text or '')
            case 'lsource':
                lsource.append(parse_lsource(child))
            case 'dial':
                dial.append(child.text or '')
            case 'gloss':
                gloss.append(parse_gloss(child))
    
    return Sense(stagk, stagr, pos, xref,ant, field, misc, s_inf, lsource, dial, gloss)
    


def parse_r_ele(element: ET.Element) -> R_ele:
    reb: str = ''
    re_nokanji: str = ''
    re_restr: list[str] = []
    re_inf: list[str] = []
    re_pri: list[str] = []
    for child in element:
        match child.tag:
            case 'reb':
                reb = child.text or ''
            case 're_nokanji':
                re_nokanji = child.text or ''
            case 're_restr':
                re_restr.append(child.text or '')
            case 're_inf':
                re_inf.append(child.text or '')
            case 're_pri':
                re_pri.append(child.text or '')
            case _:
                raise JMdictParseError('r_ele', child.tag)

    return R_ele(reb, re_nokanji, re_restr, re_inf, re_pri)


def parse_k_ele(element: ET.Element) -> K_ele:
    keb: str = ''
    ke_inf: list[str] = []
    ke_pri: list[str] = []
    for child in element:
        match child.tag:
            case 'keb':
                keb = child.text or ''
            case 'ke_inf':
                ke_inf.append(child.text or '')
            case 'ke_pri':
                ke_pri.append(child.text or '')
            case _: 
                raise JMdictParseError('k_eke', child.tag)

    return K_ele(keb=keb, ke_inf=ke_inf, ke_pri=ke_pri)


def parse_entry(element: ET.Element) -> Entry:
    ent_seq = 0
    k_ele: list[K_ele] = []
    r_ele: list[R_ele] = []
    sense: list[Sense] = []
    for child in element:
        match child.tag:
            case 'ent_seq': 
                ent_seq = int(child.text or 0)
            case 'k_ele': 
                k_ele.append(parse_k_ele(child))
            case 'r_ele':
                r_ele.append(parse_r_ele(child))
            case 'sense':
                sense.append(parse_sense(child))
    return Entry(ent_seq=ent_seq, k_ele=k_ele, r_ele=r_ele, sense=sense)


def load_jmdict(filename: str) -> list[Entry]:
    l_entry: list[Entry] = []
    root: ET.ElementTree = ET.parse(filename)
    
    for entry in root.iter('entry'):
        l_entry.append(parse_entry(entry))
    
    return l_entry
