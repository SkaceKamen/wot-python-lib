import wot
import os

# Use this class to read from world of tanks packages,
# without need of finding and extracting required resources
reader = wot.PackageReader()
model_reader = wot.ModelReader()

# Change this to your world of tanks path
reader.setWotPath("d:/Hry/World_of_Tanks_closed_Beta/")
reader.setCachePath("cache/")

# Extract model files
reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.primitives", "temp.primitives")
reader.extract("content/Buildings/bldEU_001_Town_house/normal/lod0/bldEU_001_Town_house_G01_01.visual", "temp.visual")

# Read model files
with open("temp.primitives", "rb") as prim:
	with open("temp.visual", "rb") as vis:
		model = model_reader.read(prim, vis)
		files = model.getObjMtl(normals=False)

		filename_obj = "test.obj"
		filename_mtl = "test.mtl"

		# Add mtl file reference to obj file
		files['obj'] = "mtllib " + filename_mtl + "\n" + files['obj']

		with open(filename_obj, "wb") as f:
			f.write(files['obj'])
		with open(filename_mtl, "wb") as f:
			f.write(files['mtl'])

# Remove temp files			
os.unlink("temp.primitives")
os.unlink("temp.visual")