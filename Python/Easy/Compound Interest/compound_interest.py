# Solution 1
def compound_interest(principal, rate, contribution, years):
  
  for i in range(1,years+1):
    interest = (principal * rate * 1) / 100
    principal = interest + principal + contribution
  
  return round(principal,2)
