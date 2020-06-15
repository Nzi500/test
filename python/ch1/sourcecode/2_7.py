# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:04:40 2018

@author: Jerry
"""

#提示輸入姓名
name=input("請輸入學生姓名:")
"""
 依序輸入三科分數

"""
chineseScore=input("國文分數:")
englishScore=input("英文分數:")
mathScore=input("數學分數:")

#因為是數值相加，故取得之輸入字串需要轉型成int
sum=int(chineseScore)+int(englishScore)+int(mathScore)
#取平均值
average=sum/3
#輸出結果
print("%s 三科總分為%d 平均分數為%f"%(name,sum,average))


