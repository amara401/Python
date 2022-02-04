#bubble sort algorithm

#Method-1
num = [10, 4, 13, 1, 3, 7]
n = len(num)
for i in range(n-1):
  for j in range(0,n-i-1):
    if num[j] > num[j+1]:
      num[j], num[j+1] = num[j+1], num[j]
      
print(num, "\n")

#Method-2
num = [10, 4, 13, 1, 3, 7, 3]
n = len(num)
for i in range(0, n):
  for j in range(0, n-i-1):
    if num[j] < num[j+1]:
      num[j], num[j+1] = num[j+1], num[j]
print(num)

#Method-3
def bubble_sort(num):
  n = len(num)
  print(n)
  for i in range(n-1):
    for j in range(n-i-1):
      if num[j] > num[j+1]:
        num[j], num[j+1] = num[j+1], num[j]

num = [10, 4, 13, 1, 3, 7, 3]
bubble_sort(num)
print(num)