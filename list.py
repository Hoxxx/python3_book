# list.py

import os

def list_cwd():
    """ 返回当前工作目录下所有文件和文件夹.
    """
    return os.listdir(os.getcwd())

def files_cwd():
    """ 返回当前工作目录下所有文件.
    """
    return [p for p in list_cwd()
            if os.path.isfile(p)]

def folders_cwd():
    """ 返回当前工作目录下所有文件夹.
    """
    return [p for p in list_cwd()
            if os.path.isdir(p)]

def list_py(path = None):
    """ 返回当前工作目录下所有.py文件.
    """
    if path == None:
        path = os.getcwd()
    return [fname for fname in os.listdir(path)
            if os.path.isfile(fname)
            if fname.endswith('.py')]    

def size_in_bytes(fname):
    """ 返回当前文件大小.
    """
    return os.stat(fname).st_size

def cwd_size_in_bytes():
    """ 返回当前工作目录下文件总大小.
    """
    total = 0
    for name in files_cwd():
        total = total + size_in_bytes(name)
    return total

def cwd_size_in_bytes2():
    """ 返回当前工作目录下文件总大小2.
    """
    return sum(size_in_bytes(f) for f in files_cwd())

def cwd_size_in_kb():
    """ 返回当前工作目录下文件总大小（KB）.
    """
    return cwd_size_in_bytes() / 1024
