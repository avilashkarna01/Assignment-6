#Q-1 Take 10 integers from user and print it on screen.
x=[]
for y in range(0,10):
    z=int(input("enter any number: "))
    x.append(z)
for y in range(0,5):
    print(x[y])
print("\n")

#Q-2 Write an infinite loop.An infinite loop never ends. Condition is always true.
i=0
while i<10:
    print("abhilash")
print("\n")

#Q-3 Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
x=[]
y=[]
for i in range (0,5):
   z=int(input("enter any number: "))
   x.append(z)
for i in range (0,5):
    a=x[i]
    z=a*a
    y.append(z)
print(y)
print("\n")

#Q-4 from a list containing ints,floats,strings,make three lists to store them separately.
l=[2,3.5,'a',2,6.5,'f']
t=[]
u=[]
v=[]
for i in l:
    if type(i)==type(8):
        t.append(i)
    if type(i)==type(8.4):
        u.append(i)
    if type(i)==type('8'):
        v.append(i)
print(t)
print(u)
print(v)
print("\n")

#Q-5 Using range(1,101), make a list containing even and odd numbers.
a=[]
b=[]
for i in range (1,101):
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)
print("\n")

#Q-6 Print the following patterns:
for i in range(4):
    for j in range(i+1):
        print("*",end='')
    print('')
print("\n")

#Q-7 Create a user defined dictionary and get keys corresponding to the value using for loop.
d={}
for i in range(0,10):
    x=input("enter the keys: ")
    y=input("enter the values: ")
    d[x]=y
print(d)
print("\n")

#Q-8 Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
l=[]
flag=0
for x in range(0,10):
    l.append(int(input("enter any number: ")))
print(l)
y=int(input("enter any number to search: s"))
for x in l:
    if x==y:
        l.remove(x)
        flag==0
print(l)
if flag==0:
    print("number not found")
