import StringIO
from chunks import *

class CompiledMap:
	chunks = {}
	debug = False
	
	def __init__(self, debug=False):
		self.debug = debug

	def setChunk(self, ident, contents):
		self.chunks[ident.lower()] = contents
		
	def getChunk(self, ident):
		return StringIO.StringIO(self.chunks.get(ident))
		
	def getMatrices(self):
		return bsmi.get(self.getChunk("bsmi"), self.debug)
		
	def getModels(self, ignore_vertices=True):
		return bsmo.get(self.getChunk("bsmo"), self.getStrings(), self.getMaterials(), self.getStaticGeometries() if not ignore_vertices else {}, self.getMatrices(), self.debug)
	
	def getStaticGeometries(self):
		return bwsg.get(self.getChunk("bwsg"))
	
	def getMaterials(self):
		return bsma.get(self.getChunk("bsma"), self.getStrings(), self.debug)
		
	def getTrees(self):
		return sptr.get(self.getChunk("sptr"), self.getStrings(), self.debug)
		
	def getWater(self):
		return bwwa.get(self.getChunk("bwwa"), self.debug)
		
	def getStrings(self):
		return bwst.get(self.getChunk("bwst"), self.debug)