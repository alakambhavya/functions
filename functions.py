def sum(a,b):
	c=a+b
	print("sum of two numbers is :",c)
sum(10,20)

print("___________")


def product(c,d):
	e=c*d
	print("product of two numbers is :",e)
product(5,30)

print("_____________")

def div(e,f):
	g=e/f
	return g
b=div(3,9)
print(b)

print("________________")

def mod(b,v):
	g=b%v
	return g
mod(3,9)
print(mod(3,9))

print("__________")

def sub(f,b):
	v=f-b
	return v
s=sub(10,20)
print(s)

print("___________")

def even_odd(n):
	if n%2==0:
		print("even number")
	else:
		print("odd number")
even_odd(15)

print("________")

def single_double(n):
	if -9 <= n <= 9:
		print("single digit number")
	elif -99 <= n <= 99:
		print("double digit number")
	else:
		print("invalid number")
single_double(12)

print("_________")

def hello(n):
	s=n
	return s
hello("hello_world")
print(hello("hello_world"))
