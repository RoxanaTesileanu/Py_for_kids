Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # questions = conditions
>>> # we combine these conditions and the responses into if statements
>>> 
>>> age= 13
>>> if age> 20 :
	print ('You\'r too old')

	
>>> age=23
>>> if age> 20 :
	print ('You\'r too old')

	
You'r too old
>>> # if the answer is true the commands in the block will be run
>>> # a block is a group of programming statements
>>> age=25
>>> if age > 20 :
	print('You are too old!')
	print ('Why are you here?')
	print ('Why aren\'t you mowing a lawn or sorting papers')

	
You are too old!
Why are you here?
Why aren't you mowing a lawn or sorting papers
>>> if age > 20 :
        print('You are too old!')
	print ('Why are you here?')
	print ('Why aren\'t you mowing a lawn or sorting papers')

	
You are too old!
Why are you here?
Why aren't you mowing a lawn or sorting papers
>>> if age > 20 :
        print('You are too old!')
	print ('Why are you here?')
	  print ('Why aren\'t you mowing a lawn or sorting papers')
	  
  File "<pyshell#20>", line 4
    print ('Why aren\'t you mowing a lawn or sorting papers')
    ^
IndentationError: unexpected indent
>>> 
>>> age=10
>>> if age>10 :
	print('you are too old for my jokes')

	
>>> age =1-
SyntaxError: invalid syntax
>>> age =10
>>> if age >= 10 :
	print ('you are too old for my jokes')

	
you are too old for my jokes
>>> age=10
>>> if age == 10 :
	print ('What\'s brown and sticky? A stick!!')

	
What's brown and sticky? A stick!!
>>> print ('want to hear a dirty joke?')
want to hear a dirty joke?
>>> age =12
>>> if age == 12 :
	print ('a pig fell in the mud')
else :
	print ("shh. it's a secret")

	
a pig fell in the mud
>>> age=8
>>> if ager ==12 :
	print ('a pig fell in the mud')
else :
	print ('shh. it\'s a secret')

	

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    if ager ==12 :
NameError: name 'ager' is not defined
>>> if age ==12 :
	print ('a pig fell in the mud')
else :
	print ('shh. it\'s a secret')

	
shh. it's a secret
>>> age=12
>>> if age ==10 :
	print ('what do you call an unhappy cranberry?)
	       
SyntaxError: EOL while scanning string literal
>>> if age ==10 :
	print ('what do you call an unhappy cranberry?')
	print('a blueberry!')
elif age==11 :
	print ('what did the green grape say tp the blue grape?')
	print('breathe! breath!')
elif age ==12 :
	print ('what did 0 say to 8?')
	print ('hi guys!')
elif age ==13 :
	print ('why wasn\'t 10 afraid of 7?')
	print ('because rather than eating 9, 78 pi')
else :
	print ('huh?')

	
what did 0 say to 8?
hi guys!
>>> if age ==10 or age==11 or age==12 or age==13 :
	print('what is 10 + 11+12+13? A mess!')
else :
	print ('huh?')

	
what is 10 + 11+12+13? A mess!
>>> if age >=10 and age<=13 :
	print ('what is 10+13? A mess!')
else :
	print ('huh?')

	
what is 10+13? A mess!
>>> age
12
>>> myval=None
>>> print(myval)
None
>>> # empty value
>>> if myval==None :
	print ('the variable myval doesn\'t have a value')

	
the variable myval doesn't have a value
>>> 
>>> age
12
>>> if age ==10 :
	print ('what\'s the best way to speak to a monster?')
	print ('from as far away as possible!')

	
>>> age=10
>>> if age ==10 :
	print ('what\'s the best way to speak to a monster?')
	print ('from as far away as possible!')

	
what's the best way to speak to a monster?
from as far away as possible!
>>> age='10'
>>> converted_age=int(age)
>>> age=10
>>> converted_age=str(age)
>>> print age
10
>>> age
10
>>> age='10'
>>> converted_age=int(age)
>>> if converted_age==10 :
	print ('what\'s the best way to speak to a monster?')
	print ('from as far away as possible!')

	
what's the best way to speak to a monster?
from as far away as possible!
>>> age='10.5'
>>> converted_age=int(age)

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    converted_age=int(age)
ValueError: invalid literal for int() with base 10: '10.5'
>>> converted_age=float(age)
>>> converted_age
10.5
>>> age='ten'
>>> converted_age=int(age)

Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    converted_age=int(age)
ValueError: invalid literal for int() with base 10: 'ten'
>>> cakes=250
>>> if cakes <=100 or cakes>=500 :
	print ('too few or too many')
else :
	print ('just right')

	
just right
>>> cakes = 600
>>> if cakes <=100 or cakes >=500 :
	print ('too few or too many')
else :
	print ('just right')

	
too few or too many
>>> cakes =600
>>> if cakes <=1000 or cakes >= 5000 :
	print ('too few or too many')
else :
	print ('just right')

	
too few or too many
>>> ninjas=5
>>> if ninjas < 10 :
	print ('I can fight those ninjas')
elif ninjas <30 :
	print ('It will be a struggle')
elif ninjas < 50 :
	print ('That\'s too many!')

	
I can fight those ninjas
>>> ninjas=15
>>> if ninjas < 10 :
	print ('I can fight those ninjas')
elif ninjas <30 :
	print ('It will be a struggle')
elif ninjas < 50 :
	print ('That\'s too many!')

	
It will be a struggle
>>> 
