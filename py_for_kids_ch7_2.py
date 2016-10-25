Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import sys
>>> print(sys.stin.readline())

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(sys.stin.readline())
AttributeError: 'module' object has no attribute 'stin'
>>> print(sys.stdin.readline())



>>> print(sys.stdin.readline())



>>> print(sys.stdin.readline())
let me think about it
let me think about it

>>> age=9
>>> if age >=10 and age<=13 :
	print ('what is 10 +13? a headacke!')
else :
	print ('huh?')

	
huh?
>>> def silly_age_joke(age) :
	if age >=10 and age<=13 :
		print ('what is 10+13? a headache!')
	else :
		print ('huh?')

		
>>> silly_age_joke(9)
huh?
>>> silly_age_joke(10)
what is 10+13? a headache!
>>> def silly_age_joke() :
	print ('How old are you?')
	age = int(sys.stdin.readline())
	if age >=10 and age<=13 :
		print ('what is 10+13? a headache!')
	else :
		print ('huh?')

		
>>> silly_age_joke()
How old are you?
33
huh?
>>> silly_age_joke()
How old are you?
10
what is 10+13? a headache!
>>> def moon_weight(weight, conv_index) :
	for x in range (0,15) :
		x=x+1
		moon_weight=weight*conv_index
		print moon_weight

		
>>> moon_weight(30, 0.25)
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
>>> def moon_weight(weight, conv_index) :
	moon_weight=weight*conv_index
	for x in range (0,15) :
		x=x+1
		moon_weight=weight*conv_index
		print moon_weight

		
>>> moon_weight(30,0.25)
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
7.5
>>> def moon_weight(weight, conv_index) :
	moon_weight=weight*conv_index
	for x in range (0,15) :
		x=x+1
		moon_weight=weight*conv_index + 0.25
		print moon_weight

		
>>> moon_weight(30, 0.25)
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
7.75
>>> def moon_weight(weight, conv_index) :
	moon_weight=weight*conv_index
	for x in range (0,15) :
		x=x+1
		moon_weight=moon_weight + 0.25
		print moon_weight

		
>>> moon_weight(30, 0.25)
7.75
8.0
8.25
8.5
8.75
9.0
9.25
9.5
9.75
10.0
10.25
10.5
10.75
11.0
11.25
>>> # moon_weight = weight * 0.165
>>> # gained_moon_weight =0.25
>>> # over 5 or 20 years
>>> def moon_weight(weight, extra_weight, time) :
	moon_weight=weight*0.165
	for x in range (0,time) :
		x=x+1
		moon_weight=moon_weight + extra_weight
		print moon_weight

		
>>> moon_weight(60, 0.25, 5)
10.15
10.4
10.65
10.9
11.15
>>> moon_weight(60, 0.25, 20)
10.15
10.4
10.65
10.9
11.15
11.4
11.65
11.9
12.15
12.4
12.65
12.9
13.15
13.4
13.65
13.9
14.15
14.4
14.65
14.9
>>> '''def moon_weight(weight, extra_weight, time) :
	moon_weight=weight*0.165
	for x in range (0,time) :
		x=x+1
		moon_weight=moon_weight + extra_weight
		print moon_weight '''
'def moon_weight(weight, extra_weight, time) :\n\tmoon_weight=weight*0.165\n\tfor x in range (0,time) :\n\t\tx=x+1\n\t\tmoon_weight=moon_weight + extra_weight\n\t\tprint moon_weight '
>>> def moon_weight :
	
SyntaxError: invalid syntax
>>> def moon_weight() :
	print ('What is your weight on Earth?')
	weight = int(sys.stdin.readline())
	print ('What is your average yearly weight gain?')
	extra_weight = int(sys.stdin.readline())
	print('How long are you planning to stay on the Moon?')
	time = int(sys.stdin.readline())
	moon_weight= weight *0.165
	for x in range (0, time) :
		x=x+1
		moon_weight = moon_weight +extra_weight
		print 'year on the Moon: %s, your weight on the Moon: %s' % (x, moon_weight)

		
>>> moon_weight()
What is your weight on Earth?
60
What is your average yearly weight gain?
0.25

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    moon_weight()
  File "<pyshell#68>", line 5, in moon_weight
    extra_weight = int(sys.stdin.readline())
ValueError: invalid literal for int() with base 10: '0.25\n'
>>> def moon_weight() :
	print ('What is your weight on Earth?')
	weight = float(sys.stdin.readline())
	print ('What is your average yearly weight gain?')
	extra_weight = float(sys.stdin.readline())
	print('How long are you planning to stay on the Moon?')
	time = int(sys.stdin.readline())
	moon_weight= weight *0.165
	for x in range (0, time) :
		x=x+1
		moon_weight = moon_weight +extra_weight
		print 'year on the Moon: %s, your weight on the Moon: %s' % (x, moon_weight)

		
>>> moon_weight()
What is your weight on Earth?
60
What is your average yearly weight gain?
0.25
How long are you planning to stay on the Moon?
10
year on the Moon: 1, your weight on the Moon: 10.15
year on the Moon: 2, your weight on the Moon: 10.4
year on the Moon: 3, your weight on the Moon: 10.65
year on the Moon: 4, your weight on the Moon: 10.9
year on the Moon: 5, your weight on the Moon: 11.15
year on the Moon: 6, your weight on the Moon: 11.4
year on the Moon: 7, your weight on the Moon: 11.65
year on the Moon: 8, your weight on the Moon: 11.9
year on the Moon: 9, your weight on the Moon: 12.15
year on the Moon: 10, your weight on the Moon: 12.4
>>> 
