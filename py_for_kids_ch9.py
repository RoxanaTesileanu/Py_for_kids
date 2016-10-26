Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> print(abs(10))
10
>>> print(abs(-10))
10
>>> steps = -3
>>> if abs(steps) >0 :
	print('character is moving')

	
character is moving
>>> print(bool(0))
False
>>> print(bool(10))
True
>>> print(bool(1))
True
>>> print(bool(-200))
True
>>> print(bool(None))
False
>>> print(bool('a'))
True
>>> # bool returns False for lists, tuples and maps that do nor contain any value, or True when they do.
>>> my_silly_list=[]
>>> print (bool(my_silly_list))
False
>>> my_silly_list=['s', 'i', 'l', 'l', 'y']
>>> print (bool(my_silly_list))
True
>>> year=input('Year of birth: ')
Year of birth: 1983
>>> if not bool(year.rstrip()) :
	print ('you need to enter a value for your year of birth')

	

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    if not bool(year.rstrip()) :
AttributeError: 'int' object has no attribute 'rstrip'
>>> year=input('Year of birth: ')
Year of birth: 

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    year=input('Year of birth: ')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> 
>>> year=input('Year of birth: ')
Year of birth: d

Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    year=input('Year of birth: ')
  File "<string>", line 1, in <module>
NameError: name 'd' is not defined
>>> year=input('Year of birth: ')
Year of birth: 1990
>>> if not bool(year.rstrip()) :
	print ('you need to enter a value for your year of birth')

	

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    if not bool(year.rstrip()) :
AttributeError: 'int' object has no attribute 'rstrip'
>>> import sys
>>> year=input('Year of birth: ')
Year of birth: 1990
>>> if not bool(year.rstrip()) :
	print ('you need to enter a value for your year of birth')

	

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    if not bool(year.rstrip()) :
AttributeError: 'int' object has no attribute 'rstrip'
>>> if not bool(sys.stdin.readline()) :
	print ('you need to enter a value for your year of birth')

	
if not bool(sys.stdin.readline()) :
	print ('you need to enter a value for your year of birth')
>>> 
>>> year=input('Year of birth: ')
Year of birth: 
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    year=input('Year of birth: ')
  File "<string>", line 1
    print ('you need to enter a value for your year of birth')
        ^
SyntaxError: invalid syntax
>>> year=input('Year of birth: ')
Year of birth: 22
>>> if not bool(year.rstrip()) :
	print ('you need to enter a value for your year of birth')

	

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    if not bool(year.rstrip()) :
AttributeError: 'int' object has no attribute 'rstrip'
>>> dir(['a','short', 'list'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(1)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> popcorn="I love popcorn"
>>> dir(popcorn)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(popcorn.upper)
Help on built-in function upper:

upper(...)
    S.upper() -> string
    
    Return a copy of the string S converted to uppercase.

>>> help(popcorn.__doc__)
no Python documentation found for "str(object='') -> string\n\nReturn a nice string representation of the object.\nIf the argument is a string, the return value is the same object."

>>> # (...) means the function is a built-in function of the string class
>>> eval('print("wow")')

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    eval('print("wow")')
  File "<string>", line 1
    print("wow")
        ^
SyntaxError: invalid syntax
>>> eval(print('wow'))
SyntaxError: invalid syntax
>>> eval('print "wow"')

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    eval('print "wow"')
  File "<string>", line 1
    print "wow"
        ^
SyntaxError: invalid syntax
>>> eval('print("wow")')

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    eval('print("wow")')
  File "<string>", line 1
    print("wow")
        ^
SyntaxError: invalid syntax
>>> print("wow")
wow
>>> eval('print("wow")')

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    eval('print("wow")')
  File "<string>", line 1
    print("wow")
        ^
SyntaxError: invalid syntax
>>> eval('10*5')
50
>>> eval("print 'wow'")

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    eval("print 'wow'")
  File "<string>", line 1
    print 'wow'
        ^
SyntaxError: invalid syntax
>>> your_calculation = input('Enter a calculation:')
Enter a calculation:12*52
>>> eval(your_calculation)

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    eval(your_calculation)
TypeError: eval() arg 1 must be a string or code object
>>> eval('12*52')
624
>>> eval(your_calculation)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    eval(your_calculation)
TypeError: eval() arg 1 must be a string or code object
>>> eval(sys.stdin.readline())


Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    eval(sys.stdin.readline())
  File "<string>", line 1
    
    ^
SyntaxError: unexpected EOF while parsing
>>> eval(input('Enter a calculation:'))
Enter a calculation:1*12

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    eval(input('Enter a calculation:'))
TypeError: eval() arg 1 must be a string or code object
>>> eval(str(your_calculation))
624
>>> 
eval(str(print("wow")))
SyntaxError: invalid syntax
>>> eval(str('print("wow")'))

Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    eval(str('print("wow")'))
  File "<string>", line 1
    print("wow")
        ^
SyntaxError: invalid syntax
>>> eval(print "wow")
SyntaxError: invalid syntax
>>> eval(str(your_calculation))
624
>>> print wow

Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print wow
NameError: name 'wow' is not defined
>>> print 'wow'
wow
>>> command = print 'wow'
SyntaxError: invalid syntax
>>> command=print('wow')
SyntaxError: invalid syntax
>>> my_small_program='''print('ham')
print ('sandwich')'''
>>> exec(my_small_program)
ham
sandwich
>>> command = '''print 'wow' '''
>>> eval(command)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    eval(command)
  File "<string>", line 1
    print 'wow'
        ^
SyntaxError: invalid syntax
>>> command = "print 'wow' "
>>> eval(command)

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    eval(command)
  File "<string>", line 1
    print 'wow'
        ^
SyntaxError: invalid syntax
>>> exec(my_small_program)
ham
sandwich
>>> exec(command)
wow
>>> # use exec to run mini programs that your Python program reads in from files.
>>> float('12')
12.0
>>> float('12.023')
12.023
>>> your_age=input('Enter your age: ')
Enter your age: 33
>>> age=float(your_age)
>>> if age>13 :
	print ('You are %s years too old!' %(age-13))

	
You are 20.0 years too old!
>>> your_year=input('Enter your year of birth:')
Enter your year of birth:1983
>>> birth_year=float(your_year)
>>> print birth_year
1983.0
>>> int(123.456)
123
>>> int('123')
123
>>> len('this is a test string)
    
SyntaxError: EOL while scanning string literal
>>> len('this is a test string')
21
>>> creature_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
>>> print(len(creature_list))
6
>>> allies_map={'Batman': 'my hero no.1',
	    'Superman': 'this was my hero no. 1',
	    'Spiderman': 'this is my last one'}
>>> print(len(allies_map))
3
>>> fruit=['apple', 'banana', 'clementine', 'dragon fruit']
>>> length=len(fruit)
>>> for x in range(0, length) :
	print ('the fruit at index %s is %s' % (x, fruit[x]))

	
the fruit at index 0 is apple
the fruit at index 1 is banana
the fruit at index 2 is clementine
the fruit at index 3 is dragon fruit
>>> numbers=[5,4,10,30,20]
>>> print (max(numbers))
30
>>> print(max(10, 300, 450, 50, 90))
450
>>> print(min(numbers))
4
>>> guess_this_number= 61
>>> player_guesses=[12,15,70,45]
>>> if max(player_guesses) > guess_this_number :
	print ('You lost')
else :
	print( 'You won')

	
You lost
>>> for x in range (0,5) :
	print (x)

	
0
1
2
3
4
>>> list(range(0,5))
[0, 1, 2, 3, 4]
>>> list(range(0,20,2))
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> count_down=list(range(40, 10, -2))
>>> count_down
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12]
>>> my_list_of_numbers=list(range(0,500, 50))
>>> print my_list_of_numbers
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> sum(my_list_of_numbers)
2250
>>> ### open files
>>> test_file=open('test.txt')
>>> test_file=open('myfile.txt', 'w')
>>> test_file.write=('this is my test file')

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    test_file.write=('this is my test file')
AttributeError: 'file' object attribute 'write' is read-only
>>> test_file.write('this is my test file')
>>> test_file.write('some more letters')
>>> test_file.close()
>>> test_file=open('myfile.txt')
>>> test_file.read()
'this is my test filesome more letters'
>>> test_file=open('myfile.txt', 'w')
>>> test_file.write(/n 'newline')
SyntaxError: invalid syntax
>>> test_file.write('/n newline')
>>> test_file.read()

Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    test_file.read()
IOError: File not open for reading
>>> test_file.close()
>>> test_file=open('myfile.txt')
>>> test_file.read()
'/n newline'
>>> mystring='a string'
>>> dir(mystring)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> split(mystring)

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    split(mystring)
NameError: name 'split' is not defined
>>> mystring.split()
['a', 'string']
>>> mystring = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
>>> list(mystring.split())
['this', 'if', 'is', 'you', 'not', 'are', 'a', 'reading', 'very', 'this', 'good', 'then', 'way', 'you', 'to', 'have', 'hide', 'done', 'a', 'it', 'message', 'wrong']
>>> strings=list(mystring.split())
>>> length = len(strings)
>>> for x in range (0, length) :
	print x

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
>>> for x in range (0, length) :
	print strings[x]

	
this
if
is
you
not
are
a
reading
very
this
good
then
way
you
to
have
hide
done
a
it
message
wrong
>>> def hidden_message (mystring) :
	strings=mystring.split()
	length=len(strings)
	for x in range (0, length)
	
SyntaxError: invalid syntax
>>> def hidden_message (mystring) :
	strings=mystring.split()
	length=len(strings)
	for x in range (0, length) :
		print strings[x]

		
>>> hidden_message('what are you going to do if I am right?')
what
are
you
going
to
do
if
I
am
right?
>>> myfile=open('myfile.txt')
>>> content=myfile.read()
>>> content
'/n newline'
>>> newfile=open('newfile.txt', 'w')
>>> newfile.write(content)
>>> newfile.close()
>>> myfile.close
<built-in method close of file object at 0x7fbf6edec930>
>>> myfile.close()
>>> def make_a_copy(filename) :
	myfile=open(str(filename))
	content=myfile.read()
	newfile=open('copied.txt', 'w')
	newfile.write(content)
	newfile.close()
	myfile.close()

	
>>> make_a_copy(myfile.txt)

Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    make_a_copy(myfile.txt)
AttributeError: 'file' object has no attribute 'txt'
>>> def make_a_copy() :
	myfile_name=input('Specify the file you want to copy:')
	myfile=open(str(myfile_name))
	content=myfile.read()
	newfile=open('copied.txt', 'w')
	newfile.write(content)
	newfile.close()
	myfile.close()

	
>>> make_a_copy()
Specify the file you want to copy:myfile.txt

Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    make_a_copy()
  File "<pyshell#179>", line 2, in make_a_copy
    myfile_name=input('Specify the file you want to copy:')
  File "<string>", line 1, in <module>
AttributeError: 'file' object has no attribute 'txt'
>>> def make_a_copy() :
	myfile_name=input('Specify the file you want to copy:')
	myfile=open(myfile_name.)
	content=myfile.read()
	newfile=open('copied.txt', 'w')
	newfile.write(content)
	newfile.close()
	myfile.close()
	
SyntaxError: invalid syntax
>>> 
>>> def make_a_copy() :
	myfile_name=input('Specify the file you want to copy within "":')
	myfile=open(myfile_name)
	content=myfile.read()
	newfile=open('copied.txt', 'w')
	newfile.write(content)
	newfile.close()
	myfile.close()

	
>>> make_a_copy()
Specify the file you want to copy within "":"myfile.txt"
>>> # it worked!
>>> 
