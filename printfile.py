# printfile.py

from list import *

def print_file1(fname):
    """ 将文件fname里每一行输出到屏幕上.
    """
    f = open(fname, 'r')
    for line in f:
        print(line, end = '')
    f.close()  # optional

def print_file2(fname):
    """ 将整个文本文件作为一个字符串进行读取输出.
    """
    f = open(fname, 'r')
    print(f.read())
    f.close()

def print_file3(fname):
    """ 字符串输出简化代码.
    """
    print(open(fname, 'r').read())
    
