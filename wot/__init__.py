from PackageReader import PackageReader
from XmlUnpacker import XmlUnpacker
from ModelReader2 import ModelReader
from ModelWriter import OBJModelWriter

import xml.etree.ElementTree as ET

def unpackXml(input_file, output_file):
	with open(input_file,"rb") as f:
		xmlr = XmlUnpacker()
		with open(output_file, "wb") as o:
			o.write(ET.tostring(xmlr.read(f), "utf-8"))
			
def readXml(input_file):
	with open(input_file,"rb") as f:
		xmlr = XmlUnpacker()
		return xmlr.read(f)