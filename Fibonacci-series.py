#Fibonacci series
a, b = 0, 1
n = int(input("Enter the number:"))
for i in range(0,n):
  print(a)
  a, b = b, a+b

print("\n")  
#method-2
a, b = 0, 1  
num = []
for i in range(0,n):
  num.append(a)
  a, b = b, a+b
print(num)

print("\n")
#Method-3
a, b = 0, 1
for i in range(0,n):
  print(a, end=',')
  a, b = b, a+b

print("\n")
#Method-4
a, b = 0, 1
for i in range(0,n):
  if a < n:
    print(a, end=',')
    a, b = b, a+b
    
print("\n")
#Method-5
a,b=0,1
while a<n:
  print(a, end=',')
  a, b = b, a+b
  
print("\n")
#Method-6  
def fib(num):
  a, b = 0, 1
  for i in range(num):
    print(a, end=",")
    a, b = b, a+b
fib(n)

print("\n")
#Method-7
print("Return a list containing the Fibonacci series up to n.")
def fib(n):
  a, b = 0, 1
  num=[]
  #for i in range(n):
  while a < n:
    num.append(a)
    a, b = b, a+b
  return num
print(fib(n))