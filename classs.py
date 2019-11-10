class stack:
	def __init__(self):
		self.stack=[]

	def display(self):
		if(len(self.stack)!=0):
			x=self.stack[::-1]
			for i in x:
				print(i,end=" ")


	def push(self,data):
		self.stack.append(data)
		
	def pop(self):
		t=self.stack.pop()
		return t
		
	def seek(self):
		try:
			return self.stack[-1]
		except:
			return -1
