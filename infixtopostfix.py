import classs
def number(a,ans,flag):
	if flag==0:
		ans=ans+" "+a
	else:
		ans=ans+a
	return ans
def co(a):
	if a==-1:
		return 1
	elif a=="(":
		return 2
	elif a=="+" or a=="-":
		return 3
	elif a=="*" or a=="/" or a=="%":
		return 4 
def operator(a,ans):
	if(a=='('):
		s.push(a)
	elif(a==')'):
		while(s.seek()!='('):
			ans=ans+" "+s.pop()
		a=s.pop()
	else:
		b=s.seek()
		if co(a)>co(b):
			s.push(a)
		else:
			while(co(a)<=co(s.seek())):
				ans=ans+" "+s.pop()
			s.push(a)
	return ans
def intopo(a,ans,flag):
	n=len(a)
	for i in range(n):
		
		if a[i]>='0' and a[i]<='9':
			ans=number(a[i],ans,flag)
			flag=1
		else:
			ans=operator(a[i],ans)
			flag=0
		
	while(s.seek()!=-1):
		ans=ans+" "+s.pop()
	return ans
s=classs.stack()
