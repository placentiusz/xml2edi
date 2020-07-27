from DocumentReader import ReadXMLDoc

start = ReadXMLDoc('document_6998268.xml')
start.getTradesman()
print(start.getTradesman().Name)