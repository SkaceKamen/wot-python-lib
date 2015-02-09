import os
import zipfile
import re
import json

class PackageReader:
	index = None
	packages = None
	cache = None
	wot = None
	
	def __init__(self, wot_path = None, cache_path = None):
		self.setWotPath(wot_path)
		self.setCachePath(cache_path)
	
	def setCachePath(self, dir):
		"""Set path where index cache can be stored."""
		self.cache = dir
		
	def setWotPath(self, dir):
		"""Set path to World of Tanks root folder."""
		self.wot = dir
	
	def isIndexCache(self):
		"""Returns if index cache exists."""
		return self.cache != None and os.path.exists(self.indexCachePath())
	
	def indexCachePath(self):
		"""Returns path to index cache."""
		return self.cache + "/index.cache"
	
	def loadIndexCache(self):
		"""Loads json encoded cache file."""
		index = None
		try:
			with open(self.indexCachePath(), 'r') as f:
					index = json.load(f)
		finally:
			return index
	
	def saveIndexCache(self):
		with open(self.indexCachePath(), 'w') as f:
			json.dump(self.index, f)
	
	def loadIndex(self):
		"""Preloads paths to all files in all packages."""
	
		#Load package list if neccessary
		if self.packages == None:
			self.loadPackageList()
		
		#Reset index
		self.index = {}
		
		#Check for cache
		if self.isIndexCache():
			self.index = self.loadIndexCache()
			if self.index != None:
				return
		
		#Walk all packages
		for name, pack in self.packages.iteritems():
			
			#In case some unusual symbols are present in name
			try:
				pack = unicode(pack)
			except UnicodeDecodeError:
				self.warn("Can't decode package name " + pack)
				continue
			
			#Load package info
			zfile = zipfile.ZipFile(pack)
			
			#Package name
			name = name[:-4]

			for file in zfile.infolist():
				#Get path and file
				(dirname, filename) = os.path.split(file.filename)
				
				#Split path to parts
				dirpath = dirname.split('/')
				
				#Last node is path node
				node = self.index
				
				#Walk nodes
				for part in dirpath:
					if not part in node:
						node[part] = {}
					node = node[part]
				
				#Add file to result node
				if filename in node:
					self.warn(file.filename + " is in multiple packages")
				else:
					node[filename] = pack
		
		if self.cache != None:
			self.saveIndexCache()
		
	def warn(self, text):
		"""Prints some kind of warning."""
		print "Warning: " + str(text)
		
	def loadPackageList(self):
		"""Loads paths to all avaible packages"""
	
		pck_re = r".*\.pkg"
		self.packages = {}
		
		base = self.wot + "/res/packages/"
		for pack in os.listdir(base):
			if os.path.isfile(base + pack) and re.match(pck_re, pack):
				self.packages[pack] = base + pack;
	
	def findFile(self, path):
		"""Returns package containing specified file."""
		
		if self.index == None:
			self.loadIndex()
			
		(dirname, filename) = os.path.split(path)
				
		#Split path to parts
		dirpath = dirname.split('/')
		
		#Last node is path node
		node = self.index
		
		#Walk nodes
		for part in dirpath:
			#Check path part existence
			if part not in node:
				return None
			
			node = node[part]
		
		#Check existence
		if filename not in node:
			return None
		
		return node[filename]
	
	def findFileHandle(self, zfile, package_file):
		for file in zfile.infolist():
			if file.filename == package_file:
				return file
		return None
	
	def extractFile(self, package_file, result_file):
		"""Extracts specified file from wot package."""
		
		package = self.findFile(package_file)
		(result_dirname, result_filename) = os.path.split(result_file)
		
		if package == None:
			raise Exception("Failed to find file '" + package_file + "'")
			
		zfile = zipfile.ZipFile(package)
		file = self.findFileHandle(zfile, package_file)
		
		if file == None:
			raise Exception("Failed to extract file '" + package_file + "'")
		
		file.filename = result_filename
		zfile.extract(file, result_dirname)

		return True
		
	def openFile(self, package_file, mode):
		"""Extracts specified file from wot package."""
		
		package = self.findFile(package_file)
		
		if package == None:
			return None
			
		zfile = zipfile.ZipFile(package)
		file = self.findFileHandle(zfile, package_file)
		
		if file == None:
			return None
		
		return zfile.open(file, mode)