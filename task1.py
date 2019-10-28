n = int(input())
if n % 1024 == 0:

n = n/1024
else:
n = n//1024 +1
print (n)
