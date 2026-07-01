print("_____1.sum of two numbers__________\n")
def sum(a,b):
	c=a+b
	print("sum of two numbers is :",c)
sum(10,20)


print("\n______2.product of two numbers_____\n")

def product(c,d):
	e=c*d
	print("product of two numbers is :",e)
product(5,30)

print("\n_______3.division of two numbers______\n")

def div(e,f):
	g=e/f
	return g
b=div(3,9)
print(b)

print("\n______4.module of two numbers________\n")

def mod(b,v):
	g=b%v
	return g
mod(3,9)
print(mod(3,9))

print("\n_______5.subtraction of two numbers_____\n")

def sub(f,b):
	v=f-b
	return v
s=sub(10,20)
print(s)

print("\n_______6.check whether number is even or odd_____\n")

def even_odd(n):
	if n%2==0:
		print("even number")
	else:
		print("odd number")
even_odd(15)

print("\n______7.finding number of digits______\n")

def single_double(n):
	if -9 <= n <= 9:
		print("single digit number")
	elif -99 <= n <= 99:
		print("double digit number")
	else:
		print("invalid number")
single_double(12)

print("\n______8.hello world_______\n")

def hello(n):
	s=n
	return s
hello("hello_world")
print(hello("hello_world"))

print("\n___________9.movie________\n")

def movie():
	hero=True
	heroine=True
	fighting=True
	set=True
	die=False
	blood=False
	print("hero:",hero)
	print("heroine:",heroine)
	print("fighting:",fighting)
	print("set:",set)
	print("die:",die)
	print("blood:",blood)
movie()

print("\n__________10.vegetables_____________\n")

def vegetables():
	v={"beans":(1,30),"carrot":(0.5,20),"beetroot":(2,50)}
	sum=v["beans"][0]*v["beans"][1]+v["carrot"][0]*v["carrot"][1]+v["beetroot"][0]*v["beetroot"][1]
	return sum	
	
v=vegetables()
print(v)

print("__________________")

def m1(a):
	print(a)
def m2(a):
	m1(a)
	print(a)
m2(10)

print("___________________")

def m(a):
	print(a)
def m1(a,b):
	print(a)
	print(b)
m(49)


