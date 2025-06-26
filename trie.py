
class TrieNode:
	def __init__(self):
		self.children = [None]*24
		self.isLeaf = False
		self.ind = 0


class Trie:
	def __init__(self):
		"""
		Initialise your data structure here.
		"""
		self.root = TrieNode()
	
	def indice(self, arr):
        
		"""
		
		"""
		current = self.root
		for num in arr:
			index = num - 1
			if not current.children[index]:
				return False
			current = current.children[index]
		return current.isLeaf and current.ind
	
	def insert(self, arr, ind) -> None:
		"""
		Inserts a word into the trie.
		"""
		current = self.root
		for num in arr:
			index = num - 1
			if not current.children[index]:
				current.children[index] = TrieNode()
			current = current.children[index]
		current.isLeaf = True
		current.ind = ind
	
	def inside(self, arr) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		current = self.root
		for num in arr:
			index = num - 1
			if not current.children[index]:
				return False
			current = current.children[index]
		return current.isLeaf
	
	def remove(self, arr):
		"""
		Removes the word from trie (by deactivating the leaf, the nodes above stay even without any leaf below them).
		"""
		current = self.root
		for num in arr:
			index = num - 1
			if current.children[index]:
				current = current.children[index]
		current.isLeaf = False
	
	def startsWith(self, prefix_arr) -> bool:
		"""
		Returns false or all words in the trie that starts with the given prefix.
		"""
		current = self.root
		for num in prefix_arr:
			index = num - 1
			if not current.children[index]:
				return False
			current = current.children[index]
		for i in self.traverse(current):
			yield prefix_arr + i
	
	def and_arr_pref(self, root, arr):
		"""
		Yields all word disjoint from one given.
		"""
		current = root
		if arr.__len__() == 0:
			for i in self.traverse(root):
				yield i
		else:
			for index in range(0, 24):
				if current.children[index] != None:
					if not ANDPerm[arr[0]][index + 1]:
						for i in self.and_arr_pref(current.children[index], arr[1:]):
							yield [index + 1] + i
	def enum(self, root):
		"""
		Enumerates indices of all words with leafs under given node
		"""
		current = root
		if current.isLeaf:
			yield current.ind
		else:
			for index in range(0, 24):
				if current.children[index] != None:
					for i in self.enum(current.children[index]):
						yield i
	def traverse(self, root):
		"""
		Enumerates all words with leafs under given node
		"""
		current = root
		if current.isLeaf:
			yield []
		for index in range(0, 24):
			if current.children[index] != None:
				for i in self.traverse(current.children[index]):
					yield [index + 1] + i
	
	def and_arr(self, root, arr):
		"""
		Enumerates indices of all words disjoint from given one
		"""
		current = root
		if current.isLeaf:
			yield current.ind
		else:
			for index in range(0, 24):
				if current.children[index] != None:
					if not ANDPerm[arr[0]][index + 1]:
						for i in self.and_arr(current.children[index], arr[1:]):
							yield i