# | match-case afzalligi                        | Tushuntirishi                               |
# | ------------------------------------------- | ------------------------------------------- |
# | Katta `if-elif` bloklarni soddalashtiradi   | Kodingiz chiroyli va o‘qilishi oson bo‘ladi |
# |`Tuple`, `List`, `Dict` bilan ishlaydi      | Ma’lumot strukturalariga mos keladi         |
# |`case _:` orqali default holatni belgilaydi | Har ehtimolga qarshi qamrab oladi           |

# name = input('whats your name ')

# if name == "Harry" or name == 'Hermiona' or name == 'Ron':
#     print('Griffindor')
# elif name == 'Draco':
#     print('Slytherin')
# else:
#     print('kim bu? ')

# match name:
#     case "Harry" | "Hermiona" | "Ron":
#         print('Griffindor')
#     case 'Draco':
#         print('Slytherin')
#     case _:
#         print("KIM BU ? ")


# def main():
#     x = int(input('whats number '))
#     match is_even(x):
#         case True:
#             print('juft son')
#         case False:
#             print('toq son')

# def is_even(n):
#     match n % 2 == 0:
#         case True:
#             return True
#         case False:
#             return False 

# main()


fruits = ["apple", "banana", "cherry"]

match fruits:
    case ["apple", "banana", "cherry"]:
        print("Mevalar mos tushdi!")
    case ["apple", *_]:
        print("Apple birinchi bolib turibdi")
    case _:
        print("Mevalar boshqacha")


age = int(input("Yoshingiz nechida? "))

# if age < 7:
#     print("Bogcha")
# elif age < 18:
#     print("Maktab")

# match age:
#     case a if a < 7:
#         print("Bogcha")
#     case a if a < 18:
#         print("Maktab")