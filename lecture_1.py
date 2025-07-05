# welcome back to work
# conditionls = shartlar

"""
Shartli belgilar - 
> a katta b dan
>= a katta yoki teng
< a kickina b dan
<= a kichkina yoki teng
== tengmi? deb tekshiradi a va b ni
!= teng bulmasa ishlatiladi

"""

# IF

# x = int(input('whats x '))
# y = int(input('whats y '))

# if x < y:
#     print('x is less than y')
# if x > y:
#     print('x is greater than y')
# if x == y:
#     print('x is equal to y')

# ELIF
# x = int(input('whats x '))
# y = int(input('whats y '))

# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# elif x == y:
#     print('x is equal to y')

# ELSE

# x = int(input('whats x '))
# y = int(input('whats y '))

# if x < y:
#     print('x is less than y')
# elif x > y:
#     print('x is greater than y')
# else :
#     print('x is equal to y')

# OR

# x = int(input('whats x '))
# y = int(input('whats y '))

# if x < y or x > y:
#     print('x is not equal to y')
# else :
#     print('x is equal to y')

# biza buni algoritmik jihatdan tezlashtirsak buladi

# x = int(input('whats x '))
# y = int(input('whats y '))

# if x != y:
#     print('x is not equal to y')
# else :
#     print('x is equal to y')

# AND

# Grade score project
# score = int(input('whats score '))

# if score >= 90 and score <= 100:
#     print('Grade: A')
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score < 80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print('Grade: F') 

# Bu kodni qisqaritrsak buladi bizga python yordam beradi
# score = int(input('whats score '))

# if 90 <= score <= 100:
#     print('Grade: A')
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score < 80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print('Grade: F') 

# Buni yanada qisqartirsak buladi
# score = int(input('whats score '))

# if score >= 90:
#     print('Grade: A')
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print('Grade: F') 

# Modulo
# x = int(input('whats x '))

# if x % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

# Bool = Boolen ( True and False )

# def main():
#     x = int(input('whats x '))
#     if is_even(x):
#         print('Even')
#     else:
#         print('Odd')

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# is_even funksiyamizni yanda qisqa qilib yozsak buladi misol uchun
# def is_even(n):
#     return True if n % 2 == 0 else False
# buni yanada qisqa qilsak buladi chunki bizda chiqayotgan natija shunoq ham
# true yoki false yani(0, 1)
# def is_even(n):
#     return n % 2 == 0  


# main()


# MAtch

name = input('whats your name ')

match name:
    case 'Harry':
        print('Grifindor')
    case 'Germiona':
        print('Grifindor')
    case 'Ron':
        print('Grifindor')
    case 'Draco':
        print('Slytherin')
    case _:
        print('who')

# _ bu else vazifasini bajaradi

# Tepadagi kodimizni yanada qisqartirsa buladi "or" orqali
# Lekin endi 'or' ni boshqacha yozsak buladi '|'


# name = input('whats your name ')

# match name:
#     case 'Harry' | 'Germiona' | 'Ron':
#         print('Grifindor')
#     case 'Draco':
#         print('Slytherin')
#     case _:
#         print('who')

def main():
    x = int(input('whats x '))
    match is_even(x):
        case True:
            print('Even')
        case False:
            print('Odd')

def is_even(n):
    match n % 2 == 0:
        case True:
            return True
        case False:
            return False
        
main()

