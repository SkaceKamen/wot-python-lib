from utility import *
from table import Table

def get(f, debug=False):
	table = Table(f, debug, "Matrices")
	
	matrices = []
	for item in table:
		matrices.append(unpack("<16f", item))
		
	table = Table(f, debug, "Table 2")
	
	for item in table:
		pass

	table = Table(f, debug, "Assigned models")
	
	result = {}
	index = 0
	for item in table:
		model = unp("<I", item)
		if model not in result:
			result[model] = []
		result[model].append(matrices[index])
		
		index += 1
		
	table = Table(f, debug, "Table 4")
	
	for item in table:
		pass
		
	table = Table(f, debug, "Table 5")
	
	for item in table:
		pass
		
	table = Table(f, debug, "Table 6")
	
	for item in table:
		pass
	
	return result