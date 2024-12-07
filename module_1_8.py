my_dict ={'Dmitriy': 2003, 'Vladimir': 1999, 'Alex': 1996}
print(my_dict)
print(my_dict['Dmitriy'])
print(my_dict.get('Valentin'))
my_dict.update({'Nikita': 2000, 'Kirill': 2001})
del my_dict['Alex']
print(my_dict)

my_set = {1, 2 ,3 ,1 ,2 ,3 , 'title', 'element', 'title', 'element', True}
print(my_set)
my_set.add(5)
my_set.discard(1)
print(my_set)