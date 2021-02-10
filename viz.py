# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/4/3 14:17
"""


import graphviz

dot = graphviz.Digraph(node_attr={'fontname':'SimHei'},format='png') #建立对象, engine='fdp'
dot.node('CH','储户（用户）', fontname='SimHei', shape='box')
CHLIST = ['身份证号','姓名','性别','出生年月','电话','邮箱','邮编','地址']
for i in range(len(CHLIST)):
    dot.node('CH'+str(i),CHLIST[i])
    dot.edge('CH','CH'+str(i),dir='none')
dot.node('ZH','账户',shape='box')
ZHLIST = ['账号','销户标记','账户余额']
for i in range(len(ZHLIST)):
    dot.node('ZH'+str(i),ZHLIST[i])
    dot.edge('ZH','ZH'+str(i),dir='none')
dot.node('CX', '储蓄卡', shape='box')
CXLIST = ['卡号','主/副卡']
for i in range(len(CXLIST)):
    dot.node('CX'+str(i),CXLIST[i])
    dot.edge('CX','CX'+str(i),dir='none')
print(dot) #这是指令的字符格式
dot.save('awsl')#存储指令在本地
dot.view()#查看--默认是生成在当前目录一个pdf 可以在Diagraph对象创建时设定format来改变



rel = graphviz.Digraph(node_attr={'fontname':'SimHei'},format='png') #建立对象, engine='fdp'
rel.node('JY','交易记录', fontname='SimHei', shape='diamond')
JY = "交易类型（存入/取出/还是转账）、摘要、金额、交易之前的余额、交易后的余额、交易时间".split('、')
for i in range(len(JY)):
    rel.node('JY'+str(i),JY[i])
    rel.edge('JY','JY'+str(i),dir='none')
rel.node('JX','计息',shape='diamond')
JX = "上次计息日、本次计息日、计息金额".split('、')
for i in range(len(JX)):
    rel.node('JX'+str(i),JX[i])
    rel.edge('JX','JX'+str(i),dir='none')
print(rel)
rel.save('rel')#存储指令在本地
rel.view()#查看--默认是生成在当前目录一个pdf 可以在Diagraph对象创建时设定format来改变

ER = graphviz.Digraph(node_attr={'fontname':'SimHei'},format='png',engine='neato') #建立对象, engine='fdp'
relation = ['开户','建卡','交易','计息']
for i in range(len(relation)):
    ER.node('rel'+str(i),relation[i],shape='diamond')
entity = ['用户','账户','储蓄卡']
for i in range(len(entity)):
    ER.node('en'+str(i),entity[i],shape='box')
ER.edge('en0','rel0',label="1",dir='none')
ER.edge('en1','rel0',label="n",dir='none')
ER.edge('en1','rel1',label="1",dir='none')
ER.edge('en2','rel1',label="n",dir='none')
ER.edge('en1','rel2',label="m",dir='none')
ER.edge('en1','rel2',label="n",dir='none')
ER.edge('en1','rel3',label="1",dir='none')
ER.edge('en1','rel3',label="n",dir='none')
ER.save('ER')
ER.view()



d = graphviz.Digraph(node_attr={'fontname':'SimHei'},format='png',engine='neato')
for i in range(6):
    d.node(str(i+1),'v'+str(i+1))
d.edges(['12','23','13','24','25','45','56'])
print(d)
d.view('emm')