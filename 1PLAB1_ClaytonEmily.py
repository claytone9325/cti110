Python 3.13.0rc2 (v3.13.0rc2:ec610069637, Sep  6 2024, 17:57:29) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Emily Clayton
>>> # September 22, 2024
>>> # P1LAB1
>>> # Using IDLE to get input from user and display output
>>> greeting = ("first name")
>>> first name: cynthia
SyntaxError: invalid syntax
>>> first = input("first name:")
first name:Cynthia
>>> last = input("last name:")
last name:Cupcakes
>>> last name:Cupcakes
SyntaxError: invalid syntax
>>> last name:CupcakesSyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> 
>>> print("Hello Cynthia Cupcakes! Welcome to CTI-110")
Hello Cynthia Cupcakes! Welcome to CTI-110
>>> print("first name:")
first name:
>>> star
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    star
NameError: name 'star' is not defined. Did you mean: 'str'?
>>> print("first name:")
first name:
>>> Star
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    Star
NameError: name 'Star' is not defined. Did you mean: 'str'?
>>> print(first name: Star")
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print(first name: "Star")
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("first, last name:")
...       
first, last name:
>>> print("first and last name:"),"(Emily Clayton"))
SyntaxError: unmatched ')'
>>> print("first and last name:"),"(Emily Clayton")
SyntaxError: unmatched ')'
>>> print("first and last name:","(Emily Clayton")
first and last name: (Emily Clayton
>>> print("first and last name:","Emily Clayton")
...                       
first and last name: Emily Clayton
