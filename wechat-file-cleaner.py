"""
一个重复文件处理器，主要是用来解决微信在电脑端反复存储相同文件的问题
作者 孔令仁
"""

import hashlib
import os,sys

def Str_to_MD5(inputstr):
    """
    :param inputstr: str 检测md5的pythonUFT-8字符串
    :return:
    """
    obj = hashlib.md5()#构建一个hashlib的MD5对象
    binary = inputstr.encode('utf-8')#注意要把字符串对象转换成二进制才可以
    obj.update(binary)#使用update可以将一个整体的操作分拆成多次update，效果相同
    print(obj.hexdigest())#十六进制形式的摘要digest（也可以用digest输出二进制对象）
    return

def File_to_MD5(filepath):
    """

    :param filepath: str 文件路径
    :return: hash
    """
    if not os.path.isfile(filepath):
        return
    obj = hashlib.md5()
    f = open(filepath, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        obj.update(b)
    f.close()
    return obj.hexdigest()

if __name__ == '__main__':
    print('------------')
    print('测试函数Str_to_MD5的功能')
    Str_to_MD5('abcd')
    print('------------')
    print('测试函数File_to_MD5的功能')
    print(File_to_MD5('wechat-file-cleaner-demo/test.txt'),File_to_MD5('wechat-file-cleaner-demo/test - 副本.txt'),
          File_to_MD5('wechat-file-cleaner-demo/test.txt')==File_to_MD5('wechat-file-cleaner-demo/test - 副本.txt'))
