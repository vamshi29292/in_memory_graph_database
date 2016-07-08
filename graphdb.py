import uuid
def uuidGen():
	a = uuid.uuid4()
	return a.hex

class node:
	def __init__(self,uuid,label,name,properties):
		self.uuid = uuid
		self.label = label
		self.name = name
		self.properties = properties
		self.incoming = []
		self.outgoing = []
	def __repr__(self):
		return self.name

class relation:
	def __init__(self,uuid,label,name,properties):
		self.uuid = uuid
		self.label = label
		self.name = name
		self.properties = properties
		self.pairs = []
	def __repr__(self):
		return self.name

class graph:
	def __init__(self):
		self.nodes = []
		self.relations = []
	node_name_uuid = {}
	node_uuid_index = {}
	relation_name_uuid = {}
	relation_uuid_index = {}

	def addNode(self,label,name,properties):
		uuid = uuidGen()
		self.nodes.append(node(uuid,label,name,properties))
		self.node_name_uuid[name] = uuid
		self.node_uuid_index[uuid] = len(self.nodes)-1

	def addRelation(self,label,name,properties,from_,to):  #from_ and to are uuid's of nodes
		if name not in self.relation_name_uuid:
			uuid = uuidGen()
			self.relations.append(relation(uuid,label,name,properties))
			self.relation_name_uuid[name] = uuid
			self.relation_uuid_index[uuid] = len(self.relations)-1
		self.nodes[self.node_uuid_index[from_]].outgoing.append(self.relation_name_uuid[name])
		self.nodes[self.node_uuid_index[to]].incoming.append(self.relation_name_uuid[name])
		self.relations[self.relation_uuid_index[self.relation_name_uuid[name]]].pairs.append((from_,to))

	def updateNode():
		pass

	def updateRelation():
		pass

	def deleteNode(self,uuid):
		removed = self.nodes.pop(self.node_uuid_index[uuid])
		for rel in removed.incoming:
			self.relations[self.relation_uuid_index[rel]].pairs = filter(lambda x: x[1] != rel,self.relations[self.relation_uuid_index[rel]].pairs)
		for rel in remove.outgoing:
			self.relations[self.relation_uuid_index[rel]].pairs = filter(lambda x: x[0] != rel,self.relations[self.relation_uuid_index[rel]].pairs)
		del self.node_name_uuid[removed.name]
		temp = self.node_uuid_index[removed.uuid]
		for i in self.node_uuid_index:
			if self.node_uuid_index[i] > temp:
				self.node_uuid_index[i] -= 1
		del self.node_uuid_index[removed.uuid]

	def deleteRelation(self,uuid):
		removed = self.relations.pop(self.relation_uuid_index[uuid])
		del self.relation_name_uuid[removed.name]
		for pair in removed.pairs:
			self.nodes[self.node_uuid_index[pair[0]]].outgoing.remove(pair[0])
			self.nodes[self.node_uuid_index[pair[1]]].incoming.remove(pair[1])
		temp = self.relation_uuid_index[removed.uuid]
		for i in self.relation_uuid_index:
			if self.relation_uuid_index[i] > temp:
				self.relation_uuid_index[i] -= 1
		del self.relation_uuid_index[removed.uuid]
