import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from xml.dom import minidom

class typTowaru(Enum):
    Towar = 1
    Usluga = 2
    Opakowanie = 4
    Komplet = 8

class kalkulacjaCen(Enum):
    Narzut = 0
    Marza = 1
    Zysk = 2

@dataclass
class Tradesman:
    NIP: str
    REGON: str
    Name: str
    ShortName: str
    Address: str = ''

@dataclass
class Towar:
    typTowaruDef: typTowaru
    kodIdentyfikacyjny: str
    kodTowaruDostawcy: str
    kodPaskowy: str
    nazwa: str
    opis: float
    nazwaTowaryFiskalna: float
    symbolSWWKU: str
    pkwiu: str
    jednostkaMiary: str
    symbolStawkiVat: str
    wysokoscVat: float
    symbolStawkiVatZakup: str
    wysokoscVatZakup: float
    ostatniaCenaZakNetto: float
    cenaZakWalutowa: float
    jednostkaMiaryWalutowaZakup: str
    kursWalutyKalkulacjiCeny: int
    symbolwaluty: str
    kodOpakowania: str
    jednostkaMiaryStanumin: str
    stanMinimalny: float
    sredniCzasDostawy: int
    kodIdentyfikacyjnyProdDost: str
    dataWaznosciDzien: datetime
    dataWaznosciDni: int
    jednostkaMiaryObj: str
    objetoscTwoaru: float
    iloscGodzinwJednostceUsl: float
    rodzajRoboczoGodziny: str
    cenaOtwart: bool
    uwagi: str
    podstawaKalk: kalkulacjaCen
    towarWazonyWagaEtyk: bool


class ReadXMLDoc:
    def __init__(self, filename):
        self.document = minidom.parse(filename)
        self.Tradesman = None

    def getTradesman(self):
        name = self.document.getElementsByTagName("TradesmanName")[0]
        self.Tradesman = Tradesman('1111', '1212', name.firstChild.data, 'Somename', 'street')
        return self.Tradesman

    def getProducts(self):
        products = self.document.getElementsByTagName("Product")
        for productxml in products:
            print(productxml.toString())
