immutable_var = (['apple', 3 ], 1 , 'World', True)
print(immutable_var)
immutable_var[0][0] = 'banana'
print(immutable_var)
#immutable_var[1] = 2
#print(immutable_var)
#immutable_var[2] = 'Earth'
#print(immutable_var)
#immutable_var[3] = False
#print(immutable_var)
#В первом случае получилось изменить только часть элемента(элемент списка)
#Во втором и остальных случаях не получилось изменить элементы кортежа потому, что данный вид операции не возможен, ведь кортеж это не изменяемый элемент.

mutable_list = [1, 2, 3, 'World', True]
print(mutable_list)
mutable_list[0] = 2
mutable_list[1] = 1
mutable_list[3] = 'Earth'
mutable_list[4] = False
print(mutable_list)
