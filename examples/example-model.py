import sys
# We will be loading from parent directory, nasty hack
sys.path.append('..')

import wot
import os

# Change this to your world of tanks path
reader = wot.PackageReader()
reader.setWotPath("d:/Hry/World_of_Tanks_closed_Beta/")
reader.setCachePath("cache/")

# This callback extracts texture to cache
def extractTexture(path, type):
	global reader
	
	name = os.path.split(path)[1]
	result = "cache/" + name
	
	reader.extract(path, result)
	
	return result

# Use this class to read from world of tanks packages,
# without need of finding and extracting required resources
model_reader = wot.ModelReader(True)
model_writer = wot.ColladaModelWriter(
	compress=False,
	normals=True,
	uv=True,
	material=True,
	scale=(-1,1,1),
	textureCallback=extractTexture
)
	

# Extract model files
reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.primitives_processed", "temp.primitives")
reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.visual_processed", "temp.visual")

# Read model files
with open("temp.primitives", "rb") as prim:
	with open("temp.visual", "rb") as vis:
		model = model_reader.read(prim, vis)
		model_writer.write(model, "temp.dae")

# Remove temp files			
os.unlink("temp.primitives")
os.unlink("temp.visual")