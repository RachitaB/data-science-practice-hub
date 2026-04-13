def romanToInt(s):
  
  sym_val = {
    'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
  }
  ans = 0
  i = 0
  
  while i < len(s):
    if i+1 < len(s) and sym_val[s[i+1]] > sym_val[s[i]]:
      ans += sym_val[s[i+1]] - sym_val[s[i]]
      i += 2
    else:
      ans += sym_val[s[i]]
      i += 1
    print(ans)

  
  return ans
