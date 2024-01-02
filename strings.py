import re
# PREFIXES

# bar = f'{1+2}'  # 3


# print('{}bar'.format(foo))  # foobar

i =2


for i in [2]:
    print(i)


#
# def main():
#     foo = 'foo'  # <class 'str'>
#     b_foo = b'foo'  # <class 'bytes'>
#
#
#
# s4 = "foo"
# s4 +="bar"
# print(s4)
# print('don\'t')
#
# print (s4 == "foobar") # True
# print()

foo = 'fooVal'
print(f'hello {foo}!') # hello fooVal!

num = 123.456
print(f'{num:.2f}')  # 123.46
print(f'{num:.2e}')  # 1.23e+02
print(f'{num:.2%}')  # 12345.60%


'hello'.count('l')      # 2
'hello'.find('h')       # 0
'hello'.split('l')      # ['he', '', 'o']
'hello'.partition('l')  # ('he', 'l', 'lo')
re.search('l+', 'hello')  # <_sre.SRE_Match object; span=(2, 4), match='ll'>
