## Solution 1 -> via sorting
def is_anagram(s, t):
  def sorted(string):
    st = list(string)
    n=len(st)
    for i in range(n):
      for j in range(n-i-1):
        if st[j] > st[j+1]:
          st[j],st[j+1] = st[j+1],st[j]
    return st
    
  if sorted(s)==sorted(t):
    return True

  return False

## Soltion 2 -> via Frequency calculation of each character
def is_anagram(s, t):
  def freq(string):
    
    st=list(string)
    result={}
    count = 1
    
    for char in st:
      if char in result:
        result[char] += 1
      else:
        result[char] = 1
        
    return result
    
  if freq(s).items()==freq(t).items():
    return True

  return False
