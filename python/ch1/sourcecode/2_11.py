# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:35:03 2019

@author: Jerry
"""


studentName1=input('請輸入第一位學生姓名:')
studentScore1=input('請輸入第一位學生成績:')

studentName2=input('請輸入第二位學生姓名:')
studentScore2=input('請輸入第二位學生成績:')

studentName3=input('請輸入第三位學生姓名:')
studentScore3=input('請輸入第三位學生成績:')

print("姓名   成績")
print("{0:<8}{1:>3}".format(studentName1,studentScore1))
print("{0:<8}{1:>3}".format(studentName2,studentScore2))
print("{0:<8}{1:>3}".format(studentName3,studentScore3))

sum=int(studentScore1)+int(studentScore2)+int(studentScore3)

print("總分為:{0} 平均分為:{1:6.2f}".format(sum,sum/3))