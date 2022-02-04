# EVEN or ODD number
n = int(input("Enter the number:"))
for i in range(2, n):
    if i%2 == 0:
      print(i, "is EVEN number")
    else:
      print(i, "is ODD number")
	  
print("\n")
#Method-2:
for i in range(2,n):
  if i%2 == 0:
    print(i, "is EVEN number")
    continue
  print(i, "is ODD number")
