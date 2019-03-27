Dict={1:"enter",2:"the",3:"rock",4:"stadium","name":"vakalat"}
print(Dict[1])
print(Dict["name"])
print(Dict[2])
print(Dict.get(4))
del Dict[3]
print(Dict)
Dict.clear()
print(Dict)
a=4
print(a)
A=3
print(A)
if(a%A==0):
    print("divisible")
else:
    print("not divisible")
def divisibility(a,b):
    if(a%b==0):
        print("divisible")
    else:
        print("not divisible")
divisibility(6,3)
print(3**3)
def z():
    print(x)
x=3
z()
n=[5,4,3,2,1]
print(reduce(lambda x,y:x*y,n))