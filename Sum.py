n= int(input("Enter a number:"))
a = []
for i in range(0,n+1):
  if i%2==0:
    a.append(i)
print(a[1:])
print("The sum of numbers between 1 and postive integer n is:",sum(a))