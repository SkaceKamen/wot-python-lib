import sys
# We will be loading from parent directory, nasty hack
sys.path.append('..')

# Primary library
import wot

# Used to print XML file
import xml.etree.ElementTree as ET

# Use this class to read from world of tanks packages,
# without need of finding and extracting required resources
reader = wot.PackageReader()

# Change this to your world of tanks path
reader.setWotPath("d:/Hry/World_of_Tanks_closed_Beta/")
reader.setCachePath("cache/")

# Now read file from wot packages and print it
with reader.open("spaces/05_prohorovka/space.settings", "rb") as f:
	xmlr = wot.XmlUnpacker()
	print ET.tostring(xmlr.read(f))