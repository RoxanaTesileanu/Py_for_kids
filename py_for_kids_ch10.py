Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> # Python module = a combination of functions, classes and variables.
>>> # Python uses modules to group functions and classes to make them easier to use.
>>> import turtle
>>> t= turtle.Pen()
>>> del t
>>> t= turtle.Pen()
>>> class Animal :
	def __init__(self, species, number_of_legs, color) :
		self.species=species
		self.number_of_legs=number_of_legs
		self.color=color

		
>>> harry=Animal('hipogriff', 6, 'pink')
>>> import copy
>>> harriet=copy.copy(harry)
>>> harriet.species
'hipogriff'
>>> # create and copy a list of Animal objects
>>> harry = Animal('hipoagriff', 6, 'pink')
>>> carrie = Animal('chimera', 4, 'green polka dots')
>>> billy=Animal('bogill', 0, 'paisley')
>>> my_animals=[harry, carrie, billy, harriet]
>>> more_animals= copy.copy(my_animals)
>>> more_animals[0].species
'hipoagriff'
>>> more_animals[1].species
'chimera'
>>> for x in range (0 , len(more_animals)) :
	print more_animals[x].species

	
hipoagriff
chimera
bogill
hipogriff
>>> more_animals
[<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>]
>>> len(more_animals)
4
>>> more_animals= copy.copy(my_animals)
>>> len(more_animals)
4
>>> # ahhh! it just makes a copy doesn't double them
>>> my_animals.append(more_animals)
>>> len(my_animals)
5
>>> print my_animals
[<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>, [<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>]]
>>> for x in range (0 , len(my_animals)) :
	print my_animals[x].species

	
hipoagriff
chimera
bogill
hipogriff

Traceback (most recent call last):
  File "<pyshell#36>", line 2, in <module>
    print my_animals[x].species
AttributeError: 'list' object has no attribute 'species'
>>> my_animals=[harry, carrie, billy, harriet]
>>> more_animals= copy.copy(my_animals)
>>> herd=my_animals.append(more_animals)
>>> len(herd)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    len(herd)
TypeError: object of type 'NoneType' has no len()
>>> print my_animals
[<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>, [<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>]]
>>> my_animals=[harry, carrie, billy, harriet]
>>> my_animals
[<__main__.Animal instance at 0x7f535ee7a6c8>, <__main__.Animal instance at 0x7f535eee3dd0>, <__main__.Animal instance at 0x7f535e3a89e0>, <__main__.Animal instance at 0x7f535ec57d40>]
>>> print my_animals.species

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print my_animals.species
AttributeError: 'list' object has no attribute 'species'
>>> print my_animals[0]
<__main__.Animal instance at 0x7f535ee7a6c8>
>>> my_animals=[harry, carrie, billy, harriet]
>>> my_animals[0].species = 'ghoul'
>>> print (my_animals[0].species)
ghoul
>>> print (more_animals[0].species)
ghoul
>>> print len(more_animals), len(my_animals)
4 4
>>> sally = Animal('sphinx', 4, 'sand')
>>> my_animals.append(sally)
>>> print len(more_animals), len(my_animals)
4 5
>>> new_animals=copy.deepcopy(my_animals)
>>> print (my_animals[0].species)
ghoul
>>> my_animals[0].species='wyrm'
>>> print (my_animals[0].species)
wyrm
>>> print (new_animals[0].species)
ghoul
>>> 
>>> import keyword
>>> print (keyword.iskeyword('if'))
True
>>> print (keyword.iskeyword('roxana'))
False
>>> print (keyword.kwlist)
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> import random
>>> print(random.randint(1,100))
19
>>> random.randint(100, 1000)
942
>>> random.randint(1000, 5000)
1980
>>> num =random.randint(1,100)
>>> while True :
	print ('Guess a number between 1 and 100')
	guess=input()
	i=int(guess)
	if i ==num :
		print ('You guessed right')
		break
	elif i<num :
		print ('Try higher')
	elif i> num :
		print ('Try lower')

		
Guess a number between 1 and 100
40
Try higher
Guess a number between 1 and 100
60
Try lower
Guess a number between 1 and 100
50
Try higher
Guess a number between 1 and 100
55
Try higher
Guess a number between 1 and 100
57
Try higher
Guess a number between 1 and 100
58
You guessed right
>>> 
==================== RESTART: /home/roxana/private/Py_for_kids/guess_game.py ====================

Traceback (most recent call last):
  File "/home/roxana/private/Py_for_kids/guess_game.py", line 1, in <module>
    num =random.randint(1,100)
NameError: name 'random' is not defined
>>> 
==================== RESTART: /home/roxana/private/Py_for_kids/guess_game.py ====================
Guess a number between 1 and 100
60
Try higher
Guess a number between 1 and 100
67
Try higher
Guess a number between 1 and 100
80
Try higher
Guess a number between 1 and 100
88
Try higher
Guess a number between 1 and 100
90
Try higher
Guess a number between 1 and 100
92
Try higher
Guess a number between 1 and 100
95
Try higher
Guess a number between 1 and 100
99
Try lower
Guess a number between 1 and 100
98
You guessed right
>>> 
==================== RESTART: /home/roxana/private/Py_for_kids/guess_game.py ====================
Guess a number between 1 and 100
70
Try lower
Guess a number between 1 and 100
60
Try lower
Guess a number between 1 and 100
50
Try lower
Guess a number between 1 and 100
40
Try lower
Guess a number between 1 and 100
30
Try lower
Guess a number between 1 and 100
20
Try lower
Guess a number between 1 and 100
10
You guessed right
>>> import random
>>> desserts = ['ice cream', 'pancakes', 'brownies', 'cookies', 'candy']
>>> print(random.choice(desserts))
ice cream
>>> print(random.choice(desserts))
candy
>>> print (random.choice(desserts))
cookies
>>> print (random.choice(desserts))
pancakes
>>> print (random.choice(desserts))
cookies
>>> print (random.choice(desserts))
ice cream
>>> print (random.choice(desserts))
brownies
>>> print (random.choice(desserts))
pancakes
>>> random.shuffle(desserts)
>>> desserts
['candy', 'cookies', 'ice cream', 'brownies', 'pancakes']
>>> random.shuffle(desserts)
>>> desserts
['brownies', 'candy', 'pancakes', 'cookies', 'ice cream']
>>> import sys
>>> sys.exit
<built-in function exit>
>>> sys.exit()
>>> sys.exit()
>>> v= sys.stdin.readline()
He who laughs last thinks slowest
>>> print (v)
He who laughs last thinks slowest

>>> myinput=input()
bla

Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    myinput=input()
  File "<string>", line 1, in <module>
NameError: name 'bla' is not defined
>>> myinput=input("say something:")
say something:bla

Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    myinput=input("say something:")
  File "<string>", line 1, in <module>
NameError: name 'bla' is not defined
>>> sys.stdout.write('write smth')
write smth
>>> print (sys.version)
2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609]
>>> import time
>>> print (time.time())
1477486647.45
>>> def lots_of_numbers(max) :
	for x in range(0, max) :
		print (x)

		
>>> lots_of_numbers(1000)
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
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
939
940
941
942
943
944
945
946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
964
965
966
967
968
969
970
971
972
973
974
975
976
977
978
979
980
981
982
983
984
985
986
987
988
989
990
991
992
993
994
995
996
997
998
999
>>> def lots_of_numbers(max) :
	t1=time.time()
	for x in range (0, max) :
		print (x)
	t2=time.time()
	print ('it took %s seconds' % (t2-t1))

	
>>> lots_of_numbers(500)
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
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
it took 4.29526185989 seconds
>>> print(time.asctime())
Wed Oct 26 16:03:24 2016
>>> t=(2007, 5, 27, 10, 30, 48, 6,0,0)
>>> print (time.asctime(t))
Sun May 27 10:30:48 2007
>>> print(time.localtime())
time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=16, tm_min=6, tm_sec=19, tm_wday=2, tm_yday=300, tm_isdst=1)
>>> t=time.localtime()
>>> year=t[0]
>>> month=t[1]
>>> print year , monthr
2016

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    print year , monthr
NameError: name 'monthr' is not defined
>>> print year, month
2016 10
>>> for x in range (0, 10)
SyntaxError: invalid syntax
>>> for x in range (0,10) :
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
>>> for x in range (0,1)) :
	
SyntaxError: invalid syntax
>>> for x in range (0,10) :
	print (x)
	time.sleep(1)

	
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
>>> # using the pickle module to save information
>>> 
