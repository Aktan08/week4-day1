# Напишите программу, в которой указан список целых чисел. Замените
# отрицательные на -1, положительные на 1, и оставить ноль без
# изменений.(Используйте встроенные функции, чтобы решить эту задачу)
def func(x):
    if x<0:
        return -1
    elif x>0:
        return 1
    else:
        return 0
my_list= list(map(func,range(-10,10)))

print(my_list)
