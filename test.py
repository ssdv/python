import math as ma

print (ma.sqrt(1 + 1))

a = 1
if a == 1:
    print 1
    a = 10
elif a == 2:
    print 2
elif a == 10:
    print 3
else:
    print "Qwerty"
print a
i = 1
while i < 10:
    print i
    i = i + 1

print ("total=" + str(i))
print (i)


fib1 = 0
fib2 = 1
i = 1
while i < 10:
    fibSum = fib2 + fib1
    fib1 = fib2
    fib2 = fibSum
    if i >= 2 and i <= 5:
        print fib1,
    i = i + 1
print ""
a = input("Enter your age")
print a


