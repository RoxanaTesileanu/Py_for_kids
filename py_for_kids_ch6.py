Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # for loops repeat things like other programming statements and blocks of code automatically
>>> for x in range (0,5) :
	print ('hello')

	
hello
hello
hello
hello
hello
>>> range(0,5)
[0, 1, 2, 3, 4]
>>> print (list(range(10,20))
)
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> for x in range (0,5) :
	print ('hello %s' % x)

	
hello 0
hello 1
hello 2
hello 3
hello 4
>>> x=0
>>> print('hello %s' % x)
hello 0
>>> x=1
>>> print('hello %s' % x)
hello 1
>>> x=2
>>> print('hello %s' %x)
hello 2
>>> x=3
>>> print ('hello %s' %x)
hello 3
>>> x=4
>>> print ('hello %s' %x)
hello 4
>>> wizard_list = ['spider legs', 'toe of frog', 'snail tongue',
'bat wing', 'slug butter', 'bear burp']
>>> for i in wizard_list :
	print (i)

	
spider legs
toe of frog
snail tongue
bat wing
slug butter
bear burp
>>> hugehairypants = ['huge', 'hairy', 'pants']
>>> for i in hugehairypants :
	print (i)
	print (i)

	
huge
huge
hairy
hairy
pants
pants
>>> hugehairypants = ['huge', 'hairy', 'pants']
>>> for i in hugehairypants :
	print (i)
	for j in hugehairypants :
		print (j)

		
huge
huge
hairy
pants
hairy
huge
hairy
pants
pants
huge
hairy
pants
>>> 20 + 10*365 -3*52
3514
>>> found_coins=20
>>> magic_coins=70
>>> stolen_coins=3
>>> coins=found_coins
>>> for week in range(1,53) :
	coins = coins + magic_coins - stolen_coins
	print ('Week %s = %s' % (week, coins))

	
Week 1 = 87
Week 2 = 154
Week 3 = 221
Week 4 = 288
Week 5 = 355
Week 6 = 422
Week 7 = 489
Week 8 = 556
Week 9 = 623
Week 10 = 690
Week 11 = 757
Week 12 = 824
Week 13 = 891
Week 14 = 958
Week 15 = 1025
Week 16 = 1092
Week 17 = 1159
Week 18 = 1226
Week 19 = 1293
Week 20 = 1360
Week 21 = 1427
Week 22 = 1494
Week 23 = 1561
Week 24 = 1628
Week 25 = 1695
Week 26 = 1762
Week 27 = 1829
Week 28 = 1896
Week 29 = 1963
Week 30 = 2030
Week 31 = 2097
Week 32 = 2164
Week 33 = 2231
Week 34 = 2298
Week 35 = 2365
Week 36 = 2432
Week 37 = 2499
Week 38 = 2566
Week 39 = 2633
Week 40 = 2700
Week 41 = 2767
Week 42 = 2834
Week 43 = 2901
Week 44 = 2968
Week 45 = 3035
Week 46 = 3102
Week 47 = 3169
Week 48 = 3236
Week 49 = 3303
Week 50 = 3370
Week 51 = 3437
Week 52 = 3504
>>> # while loop
>>> for step in range (0,20) :
	print (step)

	
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
>>> step=0
>>> while step<10000 :
	print(step)
	if tired == True :
		break
	elif badweather==True :
		break
	else :
		step = step +1

		
0

Traceback (most recent call last):
  File "<pyshell#58>", line 3, in <module>
    if tired == True :
NameError: name 'tired' is not defined
>>> x=45
>>> y=80
>>> while x<50 and y<100 :
	x= x+1
	y= y+1
	print (x,y)

	
(46, 81)
(47, 82)
(48, 83)
(49, 84)
(50, 85)
>>> # the condition for the while loop is just TRUE
>>> for x in range(0, 20) :
	print('hello %s' % x)
	if x<9 :
		break

	
hello 0
>>> for x in range(0, 20) :
	print('hello %s' % x)
	if x<9 :
	break
  File "<pyshell#72>", line 4
    break
        ^
IndentationError: expected an indented block
>>> 
>>> for x in range(0, 20) :
	print('hello %s' % x)
	if x<9 :
		break

	
hello 0
>>> for x in range (1:34) :
	
SyntaxError: invalid syntax
>>> for x in range(1, 38) :
	print ('age %s' % x)
	x=x+2
	if x==33 :
		break

	
age 1
age 2
age 3
age 4
age 5
age 6
age 7
age 8
age 9
age 10
age 11
age 12
age 13
age 14
age 15
age 16
age 17
age 18
age 19
age 20
age 21
age 22
age 23
age 24
age 25
age 26
age 27
age 28
age 29
age 30
age 31
>>> for x in range(1, 38) :
	x=x+2
	print ('age %s' % x)
	if x==33 :
		break

	
age 3
age 4
age 5
age 6
age 7
age 8
age 9
age 10
age 11
age 12
age 13
age 14
age 15
age 16
age 17
age 18
age 19
age 20
age 21
age 22
age 23
age 24
age 25
age 26
age 27
age 28
age 29
age 30
age 31
age 32
age 33
>>> ingredients = ['snails', 'leeches', 'gorilla belly-buttom lint', 'caterpillar eyebrows', 'centipede toes']
>>> for ingredient in ingredients :
	for j in range(len(ingredients)) :
		print (j ingredient)
		
SyntaxError: invalid syntax
>>> for j in range(len(ingredients)) :
	print j

	
0
1
2
3
4
>>> for j in range(1,len(ingredients)) :
	print j

	
1
2
3
4
>>> for j in range(1,len(ingredients)+1) :
	print j

	
1
2
3
4
5
>>> for i in ingredients :
	for j in range(1, len(ingredients) +1) :
		print ji

		

Traceback (most recent call last):
  File "<pyshell#99>", line 3, in <module>
    print ji
NameError: name 'ji' is not defined
>>> for i in ingredients :
	for j in range(1, len(ingredients) +1) :
		print j

		
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
1
2
3
4
5
>>> for i in ingredients :
	print i

	
snails
leeches
gorilla belly-buttom lint
caterpillar eyebrows
centipede toes
>>> for i in ingredients :
	x=1
	print ((x+1) i)
	
SyntaxError: invalid syntax
>>> for i in ingredients :
	x=1
	print ((x+1)  ingredients = ['snails', 'leeches', 'gorilla belly-buttom lint', 'caterpillar eyebrows', 'centipede toes']
	       
SyntaxError: invalid syntax
>>> ingredients = ['snails', 'leeches', 'gorilla belly-buttom lint', 'caterpillar eyebrows', 'centipede toes']
>>> for i in ingredients :
	x=1
	print ((x+1) i)
	
SyntaxError: invalid syntax
>>> for i in ingredients :
	x=1
	print i

	
snails
leeches
gorilla belly-buttom lint
caterpillar eyebrows
centipede toes
>>> for i in ingredients :
	x=1
	print (x,i)

	
(1, 'snails')
(1, 'leeches')
(1, 'gorilla belly-buttom lint')
(1, 'caterpillar eyebrows')
(1, 'centipede toes')
>>> for i in ingredients :
	x=1
	print (x+1,i)

	
(2, 'snails')
(2, 'leeches')
(2, 'gorilla belly-buttom lint')
(2, 'caterpillar eyebrows')
(2, 'centipede toes')
>>> for i in ingredients :
	x=x+1
	print (x,i)

	
(2, 'snails')
(3, 'leeches')
(4, 'gorilla belly-buttom lint')
(5, 'caterpillar eyebrows')
(6, 'centipede toes')
>>> for i in ingredients :
	x=x+1
	print x i
	
SyntaxError: invalid syntax
>>> for i in ingredients :
	x=x+1
	print (x,i)

	
(7, 'snails')
(8, 'leeches')
(9, 'gorilla belly-buttom lint')
(10, 'caterpillar eyebrows')
(11, 'centipede toes')
>>> for i in ingredients :
	y=y+1
	print (y,i)

	
(86, 'snails')
(87, 'leeches')
(88, 'gorilla belly-buttom lint')
(89, 'caterpillar eyebrows')
(90, 'centipede toes')
>>> for i in ingredients :
	z=z+1
	print (z,i)

	

Traceback (most recent call last):
  File "<pyshell#125>", line 2, in <module>
    z=z+1
NameError: name 'z' is not defined
>>> z=1

for i in ingredients :
	z=z+1
	
	print (z,i)
	
>>> 
>>> z=1
>>> z=0
>>> for i in ingredients :
	z=z+1
	print(z,i)

	
(1, 'snails')
(2, 'leeches')
(3, 'gorilla belly-buttom lint')
(4, 'caterpillar eyebrows')
(5, 'centipede toes')
>>> 
for i in ingredients :
	z=z+1
	print z,i

	
6 snails
7 leeches
8 gorilla belly-buttom lint
9 caterpillar eyebrows
10 centipede toes
>>> earth_w=60*0.165
>>> moon_w=60*0.165
>>> t=15
>>> for i in range (1,t+1) :
	moon_w=moon_w + 0.165
	print i, moon_w

	
1 10.065
2 10.23
3 10.395
4 10.56
5 10.725
6 10.89
7 11.055
8 11.22
9 11.385
10 11.55
11 11.715
12 11.88
13 12.045
14 12.21
15 12.375
>>> 
