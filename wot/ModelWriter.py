import zlib

class ModelWriter(object):	
	def write(self, primitive, filename):
		pass
		
class OBJModelWriter(ModelWriter):
	material = False
	
	normals = False
	uv = False
	
	textureBase = ""
	textureCallback = None
	
	compress = False
	
	def __init__(self, material=False, normals=False, uv=False, textureBase="", textureCallback=None, compress=False):
		self.material = material
		self.normals = normals
		self.uv = uv
		self.textureBase = textureBase
		self.textureCallback = textureCallback
		self.compress = compress
	
	def baseTextureCallback(self, texture, type):
		return self.textureBase + texture
	
	def write(self, primitive, filename, filename_material=None):
		objc = "# Exported by wot-python-lib 2.0.0\n"
		mtlc = objc
		
		# Reset texture callback if needed
		if self.textureCallback is None:
			self.textureCallback = self.baseTextureCallback
		
		# Guess mtl name if needed
		if filename_material is None:
			filename_material = filename.replace(".obj", ".mtl")
		
		# Add reference to material
		if self.material:
			objc += "mtllib %s\n" % filename_material
		
		# Vertices offset kept for obejcts
		offset = 0

		# Export all render sets as separate obejcts
		for rindex, render_set in enumerate(primitive.renderSets):
			for gindex, group in enumerate(render_set.groups):				
				material = group.material
				
				name = "set_%d_group_%d" % (rindex, gindex)
				material_name = material.identifier if material.identifier is not None else name
				
				objc += "o %s\n" % name
				
				# Create material if requested
				if self.material:
					objc += "usemtl %s\n" % material_name
					mtlc += "newmtl %s\n" % material_name
					
					if material.diffuseMap:
						mtlc += "map_Kd %s\n" % self.textureCallback(material.diffuseMap, "diffuseMap")
					if material.specularMap:
						mtlc += "map_Ks %s\n" % self.textureCallback(material.specularMap, "specularMap")
					if material.normalMap:
						mtlc += "map_norm %s\n" % self.textureCallback(material.normalMap, "normalMap")
				
				# Add group vertices
				for vertex in group.vertices:
					objc += "v %f %f %f\n" % vertex.position
					if self.normals:
						objc += "vn %f %f %f\n" % vertex.normal
					if self.uv:
						objc += "vt %f %f\n" % (vertex.uv[0], -vertex.uv[1])
				
				# Decide faces format
				format = 0
				if not self.normals and not self.uv:
					format = 1
				elif self.normals and not self.uv:
					format = 2
				elif not self.normals and self.uv:
					format = 3
				
				# Write indices
				for i in range(0, len(group.indices) - 3, 3):
					l1 = offset + group.indices[i] + 1
					l2 = offset + group.indices[i + 1] + 1
					l3 = offset + group.indices[i + 2] + 1
					
					if format == 0:
						objc += "f %d/%d/%d %d/%d/%d %d/%d/%d\n" % (l1, l1, l1, l2, l2, l2, l3, l3, l3)
					elif format == 1:
						objc += "f %d %d %d\n" % (l1, l2, l3)
					elif format == 2:
						objc += "f %d//%d %d//%d %d//%d\n" % (l1, l1, l2, l2, l3, l3)
					elif format == 3:
						objc += "f %d/%d %d/%d %d/%d\n" % (l1, l1, l2, l2, l3, l3)
					
				offset += len(group.vertices)
		
		# Compress if needed
		if self.compress:
			objc = zlib.compress(objc)
			mtlc = zlib.compress(mtlc)
		
		# Save to result filename
		with open(filename, "wb") as f:
			f.write(objc)
		
		if self.material:
			with open(filename_material, "wb") as f:
				f.write(mtlc)
			
		return filename, filename_material