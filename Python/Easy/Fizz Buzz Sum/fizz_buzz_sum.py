def fizz_buzz_sum(target):
  
  ans=0
  
  for i in range(3,target):
    if i%3==0 or i%5==0:
     ans += i
  
  return ans
  
