my_dict = {'Evgeny' : 1997, 'Phone' : 9034420733, 'City' : 'Kislovodsk'}
print("Dict: ", my_dict)
print("Existing value: ", my_dict['Evgeny'])
print("Not existing value: ", my_dict.get('Denis'))
my_dict.update({'DropWave': 44433322211, 'Max': 9034420733})
#my_dict = set(my_dict)
print('Deleted value: ', my_dict.pop('City'))
print("Modified dictionary: ", my_dict)

my_set = {1, 2, 1, 4, 4, 'Яблоко', 'Апельсин', 43.123}
print(my_set)
my_set.add(10)
my_set.add(15)
print("Set: ", my_set)
my_set.discard('Апельсин')
print("Modified set: ", my_set)