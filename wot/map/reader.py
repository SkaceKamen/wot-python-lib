from map import CompiledMap
from struct import unpack

class CompiledMapReader:
	def __init__(self):
		pass
	
	def get_row_section(self, section):
		return {
			'header'	: unpack('4s', section[0:4])[0].decode('UTF-8'),
			'int1'		: unpack('<I', section[4:8])[0],
			# int2 -> section start
			'int2'		: unpack('<I', section[8:12])[0],
			'int3'		: unpack('<I', section[12:16])[0],
			# int4 -> section length
			'int4'		: unpack('<I', section[16:20])[0],
			'int5'		: unpack('<I', section[20:24])[0]
		}
		
	
	def load(self, filename):
		map = CompiledMap()
		
		with open(filename, "rb") as f:
			main = self.get_row_section(f.read(24))
			tables = []
			
			if main['header'] != "BWTB":
				raise Exception("Uknown first chunk")
			
			for i in range(main['int5']):
				tables.append( self.get_row_section(f.read(24)) )
			
			for row in tables:
				f.seek(row['int2'])
				map.setChunk(row['header'], f.read(row['int4']))
		
		return map