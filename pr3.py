#1
print('Завдання 1:')

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
def check(a,b,c):
    if a > 0:
        a= a**2
    elif a < 0:
        a= a**4
    else:
        print('a = 0')
    
    if b > 0:
        b= b**2
    elif b < 0:
        b= b**4
    else:
        print('b = 0')
    
    if c > 0:
        c= c**2
    elif c < 0:
        c= c**4
    else:
        print('c = 0')
        
    return a,b,c

print(check(a,b,c))

# 2
print('Завдання 2:')

x1 = float(input('Введіть координату x першої точки'))
y1 = float(input('Введіть координату y першої точки'))

x2 = float(input('Введіть координату x другої точки'))
y2 = float(input('Введіть координату y другої точки'))

def coord(x1,y1,x2,y2):
    f= ((0 - x1) * (0 - x1) + (0 - y1) * (0 - y1))**2
    s= ((0 - x2) * (0 - x2) + (0 - y2) * (0 - y2))**2
    
    if f<s:
        return "Перша точка знаходиться ближче до початку координат"
    elif f>s:
        return "Друга точка знаходиться ближче до початку координат"
    else: 
        return "Точки на однаковій відстані від початку"
print(coord(x1,y1,x2,y2))

#3
print('Завдання 3: ')

a = float(input('Введіть перший кут в градусах'))
b = float(input('Введіть другий кут в градусах'))
def triangle(a,b):
    if a+b != 180:
        if a ==90 or b== 90 or 180 - (a+b) == 90:
            print('Це прямокутний трикутник')
        return "такий трикутник може існувати"
    else:
        return "Нема такого трикутника"

print(triangle(a,b))

#4
print('Завдання 4:')

x=int(input('Введіть перше число: '))
y=int(input('Введіть друге число: '))

def four(x,y):
    if x!=y and x<y:
        x = (x+y)/2
        y = (x*y)*2
        return x,y
    elif x!=y and x>y: 
        x = (x*y)*2
        y = (x+y)/2
        return x,y
    else:
        return "Числа однакові"
print(four(x,y))

#5

print('Завдання 5:')

x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))

def coordCheck(x,y):
    if x == 0 and y == 0:
        return "Точка A знаходиться в початку координат."
    elif x == 0:
        return "Точка A знаходиться на вісі Y."
    elif y == 0:
        return "Точка A знаходиться на вісі X."
    elif x > 0 and y > 0:
        return "Точка A знаходиться в першому координатному куті."
    elif x < 0 and y > 0:
        return "Точка A знаходиться в другому координатному куті."
    elif x < 0 and y < 0:
        return "Точка A знаходиться в третьому координатному куті."
    else:
        return "Точка A знаходиться в четвертому координатному куті."

print(coordCheck(x,y))

#6

print("Завдання 6:")

a = int(input("Введіть число а: "))
b = int(input("Введіть число b: "))

def checkTwo(a,b):
    if a!=b:
        if a>b:
            b = a
            return f"a = {a},b = {b}"
        elif a<b:
            a = b
            return f"a = {a},b = {b}"
    else:
        a = 0
        b = 0
    return f"a = {a},b = {b}"
        
print(checkTwo(a,b))

#7

print("Завдання 7:")

a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

def neg(a,b,c):
    neg = 0
    if a<0:
        neg +=1
    if b<0:
        neg +=1
    if c<0:
        neg +=1
    return f"кількість негативних значень: {neg}"

print(neg(a,b,c))

#8

print("Завдання 8:")

def dod(a,b,c):
    dod = 0
    if a>0:
        dod +=1
    if b>0:
        dod +=1
    if c>0:
        dod +=1
    return f"кількість додатніх значень: {dod}"

print(dod(a,b,c))

#9
print("Завдання 9:")

def full(a,b,c):
    full = 0
    if a == int(a):
        full +=1
    if b == int(b):
        full +=1
    if c == int(c):
        full +=1
    return f"кількість цілих чисел: {full}"

print(full(a,b,c))

#10

print("Завдання 10:")

k = float(input("Введіть число k: "))
def last(a,b,c,k):
    dil = []
    if a%k == 0:
        dil.append(a)
    if b%k == 0:
        dil.append(b)
    if c%k == 0:
        dil.append(c)
    return f"Число k є дільником чисел: {dil}"

print(last(a,b,c,k))
