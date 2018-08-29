\# 包含所有要保留的字符的集合
keep = {'a','b','c','d','e',
        'f','g','h','i','j',
        'k','l','m','n','o',
        'p','q','r','s','t',
        'u','v','w','x','y',
        'z',
        ' ','-',"'"}
        
def normalize(s):
"""
转换为字符串
"""

result=''
for c in s.lower():
 if c in keep:
   result += c
return result
 
def normalize2(s):
"""
转换为规范的字符串
"""
return ' '.join(c for c in s.lower()
  if c in keep)
  
  
def file_stats(fname):
  """
  统计文本文件中各项信息
  """
  s=open(fname,'r').read()
  num_chars = len(s)
  num_lines = s.count('\n')
  num_words = len(normalize(s).split())
  
  print("The file '%s' has: " % fname)
  print("  %s characters" % num_chars)
  print("  %s lines" % num_lines)
  print("  %s words" % num_words)
  
  
def make_freq_dict(s):
  """
  返回一个字典，字典的键为s中的单词，值为单词ch出现的次数
  """
  s = normalize(s)
  words = s.split()
  d = {}
  for w in words:
    if w in d:
      d[w] += 1
    else:
      d[w] = 1
  return d




