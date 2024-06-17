tuple_ = 31, 'Evgeny', 'Urban', True
immutable_var = tuple_
print('Immutable tuple: ', immutable_var)
#tuple_[1] = 'Fedorov'
#print(immutable_var)        Кортеж неизменяем
#Traceback (most recent call last):
  #File "C:\Users\NoName\PycharmProjects\new1\homework5.py", line 4, in <module>
    #tuple_[1] = 'Fedorov'
    #~~~~~~^^^
#TypeError: 'tuple' object does not support item assignment

mutable_list = ([31, 'Evgeny', 'Urban', True])
print(mutable_list[1])
mutable_list[1] = 'Fedorov'
print('Mutable list: ', mutable_list)

