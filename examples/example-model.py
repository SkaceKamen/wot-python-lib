import sys
# We will be loading from parent directory, nasty hack
sys.path.append('..')

import wot
import os

# Use this class to read from world of tanks packages,
# without need of finding and extracting required resources
reader = wot.PackageReader()
model_reader = wot.ModelReader(True)
model_writer = wot.OBJModelWriter(
	compress=False,
	normals=True,
	uv=True,
	material=True
)

# Change this to your world of tanks path
reader.setWotPath("d:/Hry/World_of_Tanks_closed_Beta/")
reader.setCachePath("cache/")

# Extract model files
#reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.primitives_processed", "temp.primitives")
#reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.visual_processed", "temp.visual")
reader.extract("vehicles/chinese/Ch06_Renault_NC31/collision/Hull.visual_processed", "temp.visual")
reader.extract("vehicles/chinese/Ch06_Renault_NC31/collision/Hull.primitives_processed", "temp.primitives")

# Read model files
with open("Hull.primitives_processed", "rb") as prim:
	with open("Hull.visual_processed", "rb") as vis:
		model = model_reader.read(prim, vis)
		model_writer.write(model, "temp.obj")

# Remove temp files			
#os.unlink("temp.primitives")
#os.unlink("temp.visual")