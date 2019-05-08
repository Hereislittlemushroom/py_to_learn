class dictclass:
	dic={}
	def __init__(self,dic):
		self.dic=dic
	def del_dict(self,key):
		del self.dic[key]
	def get_dict(self,key):
		if (self.dic[key]):
			return dic[key]
		else:
			return 'not found'
	def get_key():
        