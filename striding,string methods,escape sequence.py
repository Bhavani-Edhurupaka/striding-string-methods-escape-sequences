Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="Data science"
a[::]
'Data science'
a[:::]
SyntaxError: invalid syntax
a[::1]
'Data science'
a[::2]
'Dt cec'
b="Machine Learning"
a[::3]
'Dacn'
b[::3]
'Mheeng'
b[::5]
'Mnag'
b[3::111]
'h'
a[3::11]
'a'
a[:7]
'Data sc'
b[3:11]
'hine Lea'
b[:7]
'Machine'
b[9:]
'earning'
b[::6]
'Men'
#Negative striding
d=:"python course"
SyntaxError: invalid syntax
d="python course"
a[-2:-12:-4]
'cct'
d[-2:-12:-3]
'sont'
d[-1:-5:-2]
'er'
#RUles
d[3:8:2]
'hnc'
d[9:4:3]
''
d[-6:-4:-2]
''
#REVERSE
d[::1]
'python course'
d[::-1]
'esruoc nohtyp'
#String Methods
#len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle little star"
a.count(twinkle)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.count(twinkle)
NameError: name 'twinkle' is not defined
a.count("twinkle")
2
a.count("")
28
a.count(" ")
3
a.count("k")
2
a.count(a)
1
a.count("c")
0
#find a string
a=
SyntaxError: invalid syntax
a="python"
a[4]
'o'
a.find("p")
0
a.find("h")
3
b="hello"
b.find("l")
2
b.find("hel")
0
b.find("g")
-1
#ESCAPE SEQUENCES
#\N->NEW LINE
#t->tab space
a="name\nmobile number\tmarks"
print(a)
name
mobile number	marks
a="name\\mobile number"
print(a)
name\mobile number
a"python \thello"
SyntaxError: invalid syntax
>>> a"python \thello"
SyntaxError: invalid syntax
>>> a="python \thello"
>>> print(a)
python 	hello
>>> a="python\t\thello"
>>> print(a)
python		hello
>>> #replace()
>>> a="sreshta is good girl"
>>> a.replace("sreshta","divya")
'divya is good girl'
>>> a="sreshta sreshta is a good girl"
>>> a.replace("sreshta","Divya")
'Divya Divya is a good girl'
>>> a.replace("sreshta","Divya",1)
'Divya sreshta is a good girl'
>>> a
'sreshta sreshta is a good girl'
>>> #strip
>>> #lstrip(),rstrip()
>>> a="        sreshta   "
>>> a.strip(a)
''
>>> a.strip()
'sreshta'
>>> a.lstrip()
'sreshta   '
>>> a.rstrip()
'        sreshta'
