import infixtopostfix
def ope(a,b,c):
	if a=='*':
		return c*b
	elif a=='+':
		return c+b
	elif a=='-':
		return c-b
	elif a=='/':
		return c//b

def posteval(a):
	inf=infixtopostfix.intopo(a,"",0)
	flag=0
	a=inf
	n=len(inf)
	x=0
	for i in range(n):
		if a[i]=='0' and a[i-1]==' ':
			s.push(0)
		elif(a[i]==' '):
			flag=0
			if(x!=0):
				s.push(x)
				x=0
		elif a[i]>='0' and a[i]<='9':
			y=int(a[i])
			x=x*10+y

		else:
			y=ope(a[i],s.pop(),s.pop())
			s.push(y)
	return int(s.pop())




s=infixtopostfix.s

