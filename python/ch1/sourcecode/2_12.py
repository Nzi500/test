# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:35:03 2019

@author: Jerry
"""



print('{:.2%}'.format(4/25))
print('{:.2f}'.format(4/25))

print('{:.2%}'.format(4/100))
print('{:.2f}%'.format(4/100*100))

print('{:.2%}'.format(100/4))
print('{:.2f}'.format(100/4))

print('*'*20)
#10進位轉10進位
print('{:d}'.format(10))
#10進位轉8進位
print('{:o}'.format(10))
#10進位轉16進位
print('{:x}'.format(10))
#10進位轉2進位
print('{:b}'.format(10))


"""
x=10

#二進位
print(bin(x))
#8進位
print(oct(x))
#16進位
print(hex(x))


print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))
"""
