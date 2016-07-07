def uuid():
	pass

class node:
	def __init__(self,uuid,label,properties):
		self.uuid = uuid
		self.label = label
		self.properties = properties
		self.incoming = []
		self.outgoing = []

class relation:
	def __init__(self,uuid,label,properties):
		self.uuid = uuid
		self.label = label
		self.properties = properties
		self.pairs = []

class graph:
	def __init__(self):
		self.nodes = []
		self.relations = []

	def addNode():
		pass

	def addRelation():
		pass

	def updateNode():
		pass

	def updateRelation():
		pass

	def deleteNode():
		pass

	def deleteRelation():
		pass