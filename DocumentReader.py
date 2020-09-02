import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from xml.dom import minidom


class kalkulacjaCen(Enum):
    Narzut = 0
    Marza = 1
    Zysk = 2

class TypTowaru(Enum):
    Towar = 1
    Usluga = 2
    Opakowanie = 4
    Komplet = 8


@dataclass
class Tradesman:
    NIP: str
    REGON: str
    Name: str
    ShortName: str
    Address: str = ''

@dataclass
class Towar:
    nazwa: str
    kodIdentyfikacyjny: str = ''
    kodTowaruDostawcy: str = ''
    kodPaskowy: str = ''
    opis: str = ''
    nazwaTowaryFiskalna: str = ''
    symbolSWWKU: str = ''
    pkwiu: str = ''
    jednostkaMiary: str = ''
    symbolStawkiVat: str = ''
    wysokoscVat: float = 0
    symbolStawkiVatZakup: str = ''
    wysokoscVatZakup: float = 0.
    ostatniaCenaZakNetto: float = 0.
    cenaZakWalutowa: float = 0.
    jednostkaMiaryWalutowaZakup: str = ''
    kursWalutyKalkulacjiCeny: int = 0.
    symbolwaluty: str = ''
    kodOpakowania: str = ''
    jednostkaMiaryStanumin: str = ''
    stanMinimalny: float = 0.
    sredniCzasDostawy: int = 0
    kodIdentyfikacyjnyProdDost: str = ''
    dataWaznosciDzien: datetime = datetime.now()
    dataWaznosciDni: int = 0
    jednostkaMiaryObj: str = ''
    objetoscTwoaru: float = 0.
    iloscGodzinwJednostceUsl: float = 0.0
    rodzajRoboczoGodziny: str = ''
    cenaOtwart: bool = False
    uwagi: str = ''
    podstawaKalk: kalkulacjaCen = kalkulacjaCen.Marza
    towarWazonyWagaEtyk: bool = False
    typTowaruDef: TypTowaru = TypTowaru.Towar


class ReadXMLDoc:
    def __init__(self, filename):
        self.document = minidom.parse(filename)
        self.documentET = ET.parse(filename).getroot()
        self.Tradesman = None


    def getTradesman(self):
        name = self.document.getElementsByTagName("TradesmanName")[0]
        self.Tradesman = Tradesman('1111', '1212', name.firstChild.data, 'Somename', 'street')
        return self.Tradesman

    def getDocumentHeader(self):
        docHeader = self.documentET.iter('DocumentType')
        docHeaderDict = []
        for field in docHeader:
            fields = {}
            for element in field:
                if element.tag == 'DataOfTradesman':
                    for subelement in element:
                        fields[subelement.tag] = subelement.text
                else:
                    fields[element.tag] = element.text
            docHeaderDict.append(fields)
        return docHeaderDict

    def getProducts(self):
        products = []
        test = self.documentET.iter('Product')
        for productxml in test:
            towar = {}
            for elem in productxml:
                towar[elem.tag] = elem.text
            products.append(towar)
        return products

