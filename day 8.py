Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Q2
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20
>>> a+=30
>>> a%=3
>>> print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3) and (7<4) or(18==3)) and (9>3)
False
>>> True is False
False
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> s1="Nice to have it"
>>> s2="here"
>>> print(s1+s2)
Nice to have ithere
>>> print('s1'+' '+'s2')
s1 s2
>>> print('s1'+' '+'s2')
s1 s2
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> b= a[3][1][2]
>>> print(b)
['hello']
>>> d=[s1,*a,s2]
>>> print(d)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> print(color_list_1.difference(color_list_2))
{'White', 'Black'}
>>> a=input("enter a string")
enter a stringrakshit
>>> a.lower()
'rakshit'
>>> list=list(a)
>>> set=set(list)
>>> set.remove(' ')
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    set.remove(' ')
KeyError: ' '
>>> t=len(set)
>>> if t==26:
	print("string is pangram")
	else:
		
SyntaxError: invalid syntax
>>>   else:("string is not pangram")
  
SyntaxError: unexpected indent
>>> s=input('enter a number')
enter a number5
>>> t=eval('{0}+{0}{0}+{0}{0}{0}'.format(s))
>>> print(t)
615
>>> 
>>> 7
7
>>> S=input("enter some words: ")
t=S.split()
t.sort()
print('Sorted sequence of words are : ',t)
SyntaxError: multiple statements found while compiling a single statement
>>> S=input("enter some words:")
t.sort()
print('Sorted sequence of words are :',t)
SyntaxError: multiple statements found while compiling a single statement
>>> ={'student':['Rahul','Kishore','Vidhya','Raakhi'],'marks':[57,87,67,79]}
m=(d['marks'])
print("Max marks are",(max(d['marks'])))
s=(d['student'])
print("Student who get max marks is",s[m.index(max(d['marks']))])
SyntaxError: invalid syntax
>>> d={'student':['Rahul','Kishore','Vidhya','Raakhi'],'marks':[57,87,67,79]}
m=(d['marks'])
print("Max marks are",(max(d['marks'])))
s=(d['student'])
print("Student who get max marks is",s[m.index(max(d['marks']))])
SyntaxError: multiple statements found while compiling a single statement
>>>  d={'student':['Rahul','Kishore','Vidhya','Raakhi'],'marks':[57,87,67,79]}
 
SyntaxError: unexpected indent
>>> d={'student':['Rahul','Kishore','Vidhya','Raakhi'],'marks':[57,87,67,79]
   m=(d['marks'])
   
SyntaxError: invalid syntax
>>> 