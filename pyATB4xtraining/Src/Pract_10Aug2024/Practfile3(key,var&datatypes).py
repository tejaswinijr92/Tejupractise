# ## **Keywords & Identifiers**
# - Keywords are also called Reserved Words.
# - All the keywords can be in Lower Case or Upper Case.
# - We **cannot** use a keyword as a **variable name**, **function name** or any other identifier.
# -  keywords are case-sensitive.import keyword
import keyword

print(keyword.kwlist)

# variables
# 123=3--->no only A-z & a-z
# _ underscore followed by 0 or more letters
# underscore and digits (0-9)
# case sensitive myVarible  & myvariable are two different identifier
age = 90
print(age)
_ = 50
_ = _ + 1
print(_)
abc = 123  # valid  .
print(abc)
# 123abc=90  -->not valid
_ac = 34;
print(_ac)
# 123-->not alowed
# $abc-90-->No
# Datatypes
a = 5
print(type(a))
abc = 6.2
print(type(abc))
xyz = "stringword"
print(type(xyz))
print(xyz)
pi = 3.12
print(type(pi))
isMale = True
print(type(isMale))
complexnumber = 2 + 3j
print(complexnumber.real)
print(complexnumber.imag)
age = 65
age = "text"
print(age)  # dynamically typed at run time data of variale can be changed
