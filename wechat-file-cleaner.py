"""
一个重复文件处理器，主要是用来解决微信在电脑端反复存储相同文件的问题
作者 孔令仁
"""

import hashlib, os, sys, shutil

def str_to_MD5(inputstr):
    """
    :param inputstr: str 检测md5的pythonUFT-8字符串
    :return:
    """
    obj = hashlib.md5()#构建一个hashlib的MD5对象
    binary = inputstr.encode('utf-8')#注意要把字符串对象转换成二进制才可以
    obj.update(binary)#使用update可以将一个整体的操作分拆成多次update，效果相同
    print(obj.hexdigest())#十六进制形式的摘要digest（也可以用digest输出二进制对象）
    return

def file_to_MD5(filepath):
    """

    :param filepath: str 文件路径
    :return: hash
    """
    if not os.path.isfile(filepath):
        return
    obj = hashlib.md5()
    with open(filepath, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            obj.update(b)
    return obj.hexdigest()

def build_file2hash_dict(init_path):
    """

    :param init_path: str 初始路径
    :return:
    """
    #os.walk参数：top(首个参数)-根目录，topdown-先遍历根目录，οnerrοr异常处理程序，followlinks-遍历快捷方式
    on_delete_path = os.path.join(init_path,'用来放置要删除文件的地方') #设置一个放置要删除文件的地方，因为直接删除太危险了
    os.mkdir(on_delete_path)
    md5set = set()
    cleaned = {'count': 0, 'name': []}
    for root, dirs, files in os.walk(init_path, topdown=True, followlinks=False):
        #root是当前所在目录，dirs是子目录列表，files是当前目录文件列表
        if root == on_delete_path:#这个是处理删除目标的文件夹
            continue
        for f in files:
            code = file_to_MD5(os.path.join(root, f))
            if code in md5set:
                shutil.move(os.path.join(root, f), on_delete_path)
                cleaned['name'].append(f)
                cleaned['count'] += 1
            else:
                md5set.add(code)
    print(f"已经清理{cleaned['count']}个文件,名称为：{cleaned['name']}")
    return cleaned


if __name__ == '__main__':
    print('------------')
    print('测试函数Str_to_MD5的功能')
    str_to_MD5('abcd')
    print('------------')
    print('测试函数File_to_MD5的功能')
    print(file_to_MD5('wechat-file-cleaner-demo/test.txt'), file_to_MD5('wechat-file-cleaner-demo/test - 副本.txt'),
          file_to_MD5('wechat-file-cleaner-demo/test.txt')==file_to_MD5('wechat-file-cleaner-demo/test - 副本.txt'))
    print('------------')
    print(r'测试函数build_file2hash_dict的功能，清理微信缓存C:\Users\15510\Documents\temp')
    build_file2hash_dict(r'C:\Users\15510\Documents\temp')