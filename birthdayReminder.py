# _*_coding:utf-8_*_
"""
Author: Lingren Kong
Created Time: 2020/3/30 17:23
"""
import pandas as pd
from datetime import datetime
path = r"birthday.txt"

class BirthdayReminder():

    def __init__(self,path=r"birthday.csv"):
        """

        :param path: 生日记录的文件位置
        """
        self.data = None
        self.path = path
        self.load()
        print(f"欢迎使用生日提醒程序，当前生日记录路径为{path}")

    def load(self):
        """

        :return:
        """
        try:
            self.data = pd.read_csv(self.path,encoding='UTF-8')
            print("数据加载成功")
        except:
            print("加载失败")
        print(self.data)

    def dump(self):
        self.data.to_csv(self.path,encoding='UTF-8',index=None)

    def get_constell(self, month, day):
        date_sep = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
        constellations = ("摩羯", "水瓶", "双鱼", "白羊", "金牛", "双子", "巨蟹", "狮子", "处女", "天秤", "天蝎", "射手", "摩羯")
        if day < date_sep[month-1]:
            return constellations[month-1]
        else:
            return constellations[month]

    def add(self,name,month,day):
        self.data.loc[len(self.data)] = [name,month,day]#, self.get_constell(month,day)]
        self.dump()

    def display(self):
        month = int(datetime.now().month)
        print(self.data[(self.data['月份']==month)|(self.data['月份']==month+1)])

if __name__ =='__main__':
    obj = BirthdayReminder()
    obj.display()
