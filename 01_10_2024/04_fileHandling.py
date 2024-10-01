#files
import os

#acceder a un fichero
txt_file = open("01_10_2024/my_file.txt", "r+")
#print(txt_file.read())
#txt_file.write("Hello World")   #io.UnsupportedOperation: not wr
#print(txt_file.readline())

for line in txt_file.readlines():
    print(line)

txt_file.write("\naunqeu tambien puedo escribir")
print(txt_file.read())

#crea un fichero desde aca
txt_2 = open("01_10_2024/my_file_2.txt", "w+")
txt_2.write("Hello World\n creado desde el 04\n hola\n hola")


#json file
# es un formato de intercambio de datos, clave-valor, muy utilizado en apis
import json

json.dump({"name": "John", "age": 30, "city": "New York"}, open("01_10_2024/my_json.json", "w+"))
print(json.load(open("01_10_2024/my_json.json")))

json_file = open("01_10_2024/my_json2.json", "w+")
my_test = {
    "name": "carlos",
    "age": 50,
    "city": "acapulco"
}
json.dump(my_test, json_file, indent=4)
json_file.close()
#como modificamos
json_dict = json.load(open("01_10_2024/my_json2.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])    

#scv file
import csv
csv_file = open("01_10_2024/my_csv.csv", "w+")
#como se escribe
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "age", "city"])
csv_writer.writerow(["John", 30, "New York"])
csv_writer.writerow(["Carlos", " ", "Acapulco"])

csv_file.close()


#.xlsx
#xml, es 
import xml 
#como se crea un fichero  xml
xml_file = open("01_10_2024/my_xml.xml", "w+")
xml_file.write("<name>John</name>")
xml_file.write("<age>30</age>")
xml_file.write("<city>New York</city>")
xml_file.close()
