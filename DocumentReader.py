import xml.etree.ElementTree as ET
from dataclasses import dataclass
from xml.dom import minidom


@dataclass
class Tradesman:
    NIP: str
    REGON: str
    Name: str
    ShortName: str
    Address: str = ''

@dataclass
class Product:
    ProductName: str
    ProductSymbol: str
    ProductType: str
    ProductUnit: str
    ProductCurrency: str
    ProductQuantity: float
    ProductGrossPrice: float
    ProductVatRate: str


class ReadXMLDoc:
    def __init__(self, filename):
        self.document = minidom.parse(filename)
        self.Tradesman = None

    def getTradesman(self):
        name = self.document.getElementsByTagName("TradesmanName")[0]
        self.Tradesman = Tradesman('1111', '1212', name.firstChild.data, 'Somename', 'street')
        return self.Tradesman
