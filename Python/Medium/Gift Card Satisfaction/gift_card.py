# Solution

def max_satisfaction(expectations, cards):
  ans = 0
  expectations.sort()
  cards.sort()
  i = 0
  j = 0
  while i<len(expectations) and j<len(cards):
    if expectations[i] <= cards[j]:
      i += 1
      ans += 1
    
    j+=1
  return ans
   
