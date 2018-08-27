# write.py

import os

def make_story1():
    """ 写入文本文件.
    """
    f = open('story.txt', 'w')
    f.write('Mary had a little lamb,\n')
    f.write('and then she had some more.\n')
    
def make_story2():
    """ 写入文本文件,如果story.txt存在,放弃操作.
    """
    if os.path.isfile('story.txt'):
        print('story.txt already exists; nothing written')
    else:
        f = open('story.txt', 'w')
        f.write('Mary had a little lamb,\n')
        f.write('and then she had some more.\n')

def add_to_story(line, fname = 'story.txt'):
    """ 附加到文本文件末尾.
    """
    f = open(fname, 'a')
    f.write(line)

def insert_title(title, fname = 'story.txt'):
    """ 将字符串插入到文件开头.
    """
    f = open(fname, 'r+')

    temp = f.read()
    temp = title + '\n\n' + temp
    
    f.seek(0)  # 文件指针指向文件开头
    f.write(temp)
