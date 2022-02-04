#Prime Numbers
n = int(input("Enter the number:"))
for i in range(2, n):
  for j in range(2, i):
    if i%j == 0:
      print(i, "Is NOT prime")
      break
  else:  
    print(i, "is PRIME number")