#list.py
def list_cwd():
  return os.listdir(os.getcwd())

#返回当前工作目录下的文件
def files_cwd():
  return [p for p in list_cwd()
            if os.path.isfile(p)]

#返回当前工作目录下的文件夹
def folders_cwd():
  return [p for p in list_cwd()
            if os.path.isdir(p)]

#获取当前工作目录下的.py文件
def list_py(path = None):
  if path == None:
    path == os.getcwd()
    return [fname for fname in os.listdir(path)
      if os.path.isfile(fname)
      if fname.endswith('.py')]

#获取当前工作目录下文件的大小
def size_in_bytes(fname):
  return os.stat(fname).st_size

#获取当前工作目录下文件的总大小
def cwd_size_in_bytes():
  total=0
  for name in files_cwd():
    total = total + size_in_bytes(name)
  return total
  
def cwd_size_in_bytes2():
  return sum(size_in_bytes(f)
             for f in files_cwd())








