Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import pickle
>>> game_data={
	'player-position': 'N23 E45',
	'pockets': ['keys', 'pocket knife', 'polished stone'],
	'backpack':['rope', 'hammer', 'apple'],
	'money': 320.45
	}
>>> save_file=open('save2.dat', 'wb')
>>> pickle.dump(game_data, save_file)
>>> save_file.close()
>>> 
>>> load_file=open('save2.dat', 'rb')
>>> loaded_game_data=pickle.load(load_file)
>>> load_file.close()
>>> print(loaded_game_data)
{'money': 320.45, 'backpack': ['rope', 'hammer', 'apple'], 'player-position': 'N23 E45', 'pockets': ['keys', 'pocket knife', 'polished stone']}
>>> print (game_data)
{'money': 320.45, 'backpack': ['rope', 'hammer', 'apple'], 'pockets': ['keys', 'pocket knife', 'polished stone'], 'player-position': 'N23 E45'}
>>> # Programming puzzles
>>> import copy
>>> class Car :
	pass

>>> car1=Car()
>>> car1.wheels=4
>>> car2=car1
>>> car2.wheels=3
>>> print(car1.wheels)
3
>>> car3=copy.copy(car1)
>>> car3.wheels=
SyntaxError: invalid syntax
>>> car3.wheels=6
>>> print(car1.wheels)
3
>>> favorites_list=['laptop', 'coffee', 'milk']
>>> save_file=open('favorites.dat', 'wb')
>>> pickle.dump(favorites_list, save_file)
>>> save_file.close()
>>> load_file
