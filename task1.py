# Напишите программу, которая подсчитывает количество четных и
# нечетных чисел в списке чисел. (Используйте встроенные функции,
# чтобы решить эту задачу)

list_= range(1,10)
my_list= list(filter(lambda x: x%2==0,list_))

my_list2= list(filter(lambda x: x%2!=0,list_))

print(my_list,my_list2)