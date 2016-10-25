Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> fred=100
>>> print fred
100
>>> fred
100
>>> number_of_coins=2--
SyntaxError: invalid syntax
>>> number_of_coins=200
>>> found_coins=20
>>> magic_coins=10
>>> found_coins + magic_coins *2
40
>>> found_coins + magic_coins *2
40
>>> # lists, tuples and maps are used to store collections of thinfs
>>> # text is usually called string
>>> fred = "Why do gorillas have big nostrills? Big fingers!!"
>>> print fred
Why do gorillas have big nostrills? Big fingers!!
>>> # syntax is the arrangement and order of words
>>> # EOL means end of line
>>> # multiline strings with '''
>>> fred='''How do dinos pay their bills?
With tyrannosaurus checks!'''
>>> fred
'How do dinos pay their bills?\nWith tyrannosaurus checks!'
>>> print (fred)
How do dinos pay their bills?
With tyrannosaurus checks!
>>> # using the three single quotes '''
>>> silly_string= '''He said, "Aren't can't shouldn't wouldn't"'''
>>> print silly_string
He said, "Aren't can't shouldn't wouldn't"
>>> # use backslash \ to escape strings:
>>> single_quote_str='He said, "Aren\'t can\'t shoudn\'t wouldn\'t "'
>>> print single_quote_str
He said, "Aren't can't shoudn't wouldn't "
>>> # embed values in a str with %s
>>> myscore=1000
>>> message = 'I scored %s points'
>>> print message
I scored %s points
>>> print (message %s myscore)
SyntaxError: invalid syntax
>>> print (message %s myscore)
SyntaxError: invalid syntax
>>> print (message % myscore)
I scored 1000 points
>>> # %s is a placeholder
>>> # call print only with %
>>> print(message % 1000)
I scored 1000 points
>>> joke='%s: a device for finding furniture in the dark'
>>> bodypart1= 'toes'
>>> bodypart2='knees'
>>> print(joke % bodypart1)
toes: a device for finding furniture in the dark
>>> print(joke % bodypart2)
knees: a device for finding furniture in the dark
>>> message2= "what did no %s said to no %s? Nice blet!"
>>> print (message2 % ('one', 'two'))
what did no one said to no two? Nice blet!
>>> ######## page 31 #######
>>> 
