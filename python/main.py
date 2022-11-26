# comentário

"""
    comentario
"""

# def greetings():
#     return 'olá ivan'

# print(type(greetings))
# print(greetings())


# num = 10
# print(num)
# print(type(num))

# f_number = 5.2
# print(f_number)
# print(type(f_number))

# #string
# string = 'uma string'
# print(string)
# print(type(string))

# #booleano
# boolean = True
# f_boolean = False
# print(type(boolean))
# print(boolean)
# print(type(f_boolean))
# print(f_boolean)

# erro - tipagem forte
# print(1 + '1')

# #Estruturas condicionais
# x = 5
# if x > 5:
#     print('x é maior que 5')
# elif x == 5:
#     print('x é igual a 5')
# else:
#     print('x é menor que 5')

# #and &&
# y = 10

# if x == 5 and y == 10:
#     print('x é igual a 5 e y é igual a 10')

# #or ||
# if x == 5 or y == 10:
#     print('x é 5, ou y é 10')

# #negaçao
# if not x == 20:
#     print('x não é 20')
# else:
#     print('x é 5')

# my_str = 'olá, ivan'
# for char in my_str:
#     print(char)

# my_str = 'olá, ivan'
# for item in enumerate(my_str):
#     print(item)
#     print(type(item))

# my_str = 'olá, ivan'
# for index, elem in enumerate(my_str):
#     print(index, elem)
  
# for num in range(2,10,2):
#     print(num)

# for num in range(2, 10, 2):
#     print(num)
#     if num == 4:
#         break

# valor = 100
# template_str = f'o valor é {valor}'
# print(template_str)

# print(template_str[0])
# print(template_str[1])

# valor = 100
# template_str = f'o valor é {valor}'
# str_len = len(template_str)
# print(str_len)


# last_elem = template_str[-1]
# print(last_elem)

# # slicing
# text = 'foi pra padaria'
# # print(text[8:-1])
# padaria = text[8:len(text)]
# print(padaria)

text = 'foi pra padaria'
str_split = text.split()
print(str_split)

str_join = '_'.join(str_split)
print(str_join)

tuple = ['a', 'b']
print(tuple)
tuple_join = '_'.join(tuple)
print(tuple_join)
