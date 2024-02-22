nombre = "Axel"
print("Hola", nombre)

x=19
y=7
z1=x%y
print('The remainder of ',x,'/',y,' = ', z1)
z2=x//y
print('Integer division of ',x,' and ',y, ' = ', z2)

# city=input('Enter the name of the city where you are located: ')
# print(city)

# temperature_str=input('Enter the temperature: ')
# print(temperature_str)
# print(type(temperature_str))
# print()
# temperature_int=int(input('Enter the temperature: '))
# print(temperature_int)
# print(type(temperature_int))
# print()
# temperature_float=float(input('Enter the temperature: '))
# print(temperature_float)
# print(type(temperature_float))
# print()

# avalue= int(input('Please enter the number 10: '))
# while (avalue != 10):
#     print('Your input value is not equal to 10')
#     print('Please try again: ')
#     avalue= int(input('Enter the number 10: '))
# print('Thank you')
# print('You entered a value of 10')

# for i in range(5):
#     print(i)

# m=4
# n=3
# for i in range(m):
#     for j in range(n):
#         print('i=',i,' j=',j)


# a=2
# b=3
# alist_examp=[1,3.4,'asdf',96, True, 9.6,'zxcv',False, 2>5,a+b]
# print(alist_examp)
# print(type(alist_examp))
# print('This list contains ', len(alist_examp), ' elements')

x=[101,-45,34,-300,8,9,-3,22,5]
print()
print(x[3:8:4])
# print()
# print(x[3:])
# print(x[:4])
# print()
# print(x)
# print(x[2:3])

# print(x[3:4])
# print(x[3:5])
# print(x[3:6])
# print(x[3:7])
# print(x[3:8])
# print(x[3:9])

# print()
# print(x[-1])
# print(x[-1:-3:-1])
# print(x[-1:-len(x)-1:-1])

#explore changing to uppercase and lowercase
a='good'
c=a.upper()
d=c.lower()
print(c)
print(d)
 
#join a list of strings together with a space in between the strings
b='morning'
e=' '.join([a,b,'today'])
print(e)
 
#find a string within a string
#find method returns the first index where string was found
x='a picture is worth a thousand words'
x1=x.find('picture')
print(x1)
x2=x.find('worth')
print(x2)
x3=x.find('words')
print(x3)
 
#split up a string into a list of smaller strings
#use the ' ' space character as the boundary (delimiter) to split up the string
y=x.split(' ')
print(y)
print(type(y))
 
#try the replace method ...
z=x.replace('thousand', 'million')
print(x)
print(z)

# import matplotlib.pyplot as plt
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# plt.plot(x,y)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Test Plot')
# plt.show()
# plt.savefig('plot1.png')

def findval(alist,x):
    #alist is the input list
    #x is the value being searched for
    #This function returns a bool True if found
    #and returns a bool False if not found
    for val in alist:
        if (val==x):
            return True
    return False
 
#end function definitions
#=====================
#main code begins here ...
 
a=[2,3,4,5,6,7,8]
print(findval(a,4))
print(findval(a,29))
b=[45,34,78,89]
print(findval(b,45))
print(findval(b,1470))


import math
a=math.exp(1)
print(a)
b=math.pi
print(b)
x=100
print(math.log(x,10))
print(math.log10(x))
y=math.pi/2
print(math.cos(y))
print(math.sin(y))
y=8
z=1/3
print(math.pow(y,z))


import random as rn

#set the seed to system clock time
rn.seed()

#test some methods in the random module
a=rn.random()		#uniform random number between 0 and 1
print(a)
b=rn.uniform(7,20)	#uniform random number between 7 and 20
print(b)
c=rn.randint(100,200) #random integer between 100 and 200
print(c)


a={3,4,5}
b={4,5,6,7,8,9}
c=a.intersection(b)
print(c)
d=a.union(b)
print(d)
e=8
print(e in b)
print(e in a)
f=b.difference(a)
print(f)


adexamp={'NY':'Albany', 'CA': 'Sacramento','MA':'Boston'}
print(adexamp)
print(type(adexamp))

adexamp={'NY':'Albany', 'CA': 'Sacramento','MA':'Boston'}
print(adexamp)
print(type(adexamp))
 
print(adexamp['NY'])		#value is referenced by the key
adexamp['NY'] ='Buffalo'	#values are mutable
print(adexamp['NY'])		#value is referenced by the key

# Crear un set vacío
mi_set_vacio = set()

# Crear un set con algunos elementos
mi_set = {1, 2, 3, 4, 5}

# Crear un set a partir de una lista, eliminando elementos duplicados
lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5]
mi_set_desde_lista = set(lista_con_duplicados)
print(mi_set_desde_lista)  # Output: {1, 2, 3, 4, 5}

fhandle = open('examp.txt','w')
fhandle.write('This is a write example. ')
fhandle.write('Text will be sequentially written until a newline control character occurs. \n') 
fhandle.write('Then a new line will begin with \n')    
fhandle.write('and another new line, etc \n')    
fhandle.close()


f2 = open('examp.txt','r')    
print(f2.read())    #the 'read' method reads the file    
f2.close()
