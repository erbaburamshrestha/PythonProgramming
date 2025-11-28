def maxDivide(a, b):
   while a % b == 0:
      a = a / b
   return a

def isUgly(number):
   number = maxDivide(number, 2)
   number = maxDivide(number, 3)
   number = maxDivide(number, 5)
   return 1 if number == 1 else 0

def getNthUglyNumber(n):
   i = 1
   count = 1 
   while n > count:
      i += 1
      if isUgly(i):
         count += 1
   return i
 
uglyNumber = getNthUglyNumber(10)
print("10th ugly number. is ", uglyNumber)
 