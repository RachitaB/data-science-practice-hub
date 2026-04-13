# Solution 1
def compound_interest(principal, rate, contribution, years):
  
  for i in range(1,years+1):
    interest = (principal * rate * 1) / 100
    principal = interest + principal + contribution
  
  return round(principal,2)

# Solution 2
def compound_interest(principal, rate, contribution, years):
  
  final_amount = 0
  r = rate/100
  
  final_amount = principal * ((1+r)**years) + contribution * (((1+r)**years -1) /r)
  return round(final_amount,2)
