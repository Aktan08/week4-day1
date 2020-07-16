# Напишите функцию, которая будет определять палиндром ли введенная
# строка. Если да, то напечатать “True”, если нет -“False”.
def palindrom(stroka):
    if stroka == reversed(stroka):
        print(True)
    else:
        print(False)

stroka = input()
palindrom(stroka)
