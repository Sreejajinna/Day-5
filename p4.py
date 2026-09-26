'''
----Logical operators----

Types :

1. Logical AND
2. Logical OR
3. Logical NOT

----AND------
C1   C2    Result
T    T       T
T    F       F
F    T       F
F    F       F

---- OR ----
C1   C2    Result
T    T       T
T    F       T
F    T       T 
F    F       F

----NOT Operator----

'''
a=10
b=20
c=30

print(a>b and a>c)
print(a<b and a>c)
print(a<b and a<c)

print(a>b or a>c)
print(a<b or a>c)

print(a>b)
print(not(a>b))