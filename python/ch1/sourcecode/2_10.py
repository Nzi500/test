# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 17:04:40 2018

@author: Jerry
"""

#提示輸入姓名
name=input("請輸入學生姓名:")
"""
 依序輸入三科分數
 因為要取得是數值，故取得之輸入字串需要轉型成int
"""
chineseScore=int(input("國文分數:"))
englishScore=int(input("英文分數:"))
mathScore=int(input("數學分數:"))


sum=chineseScore+englishScore+mathScore
print("\n{0:<8} 國文分數:{1:>3} 英文分數:{2:>3} 數學分數:{3:>3}".format(name,chineseScore,englishScore,mathScore))
print("總分:{:^5} 平均分數:{:6.2f}".format(chineseScore+englishScore+mathScore,sum/3))




