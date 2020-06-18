# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/6/15 17:53
"""

# 三色球各3个，同色无区别，问有多少种同色不相邻排列
import itertools
okList = set()
allpos = itertools.permutations(['红','黄','蓝']*3)
for one in allpos:
    ok = True
    for i in range(len(one)-1):
        if one[i]==one[i+1]:
            ok = False
    if ok:
        okList.add(one)
len(okList)

t = set()
for i in okList:
    count = 2
    turn = {}
    turn[i[0]] = 1
    for j in range(len(i)):
        if i[j] not in turn.keys():
            turn[i[j]] = count
            count+=1
    rep = [turn[x]  for x in i]
    print(rep)
    t.add(tuple(rep))
