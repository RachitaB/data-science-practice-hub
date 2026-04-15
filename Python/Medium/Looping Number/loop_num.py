# Solution 1 (Using strings)
def is_looping(n):
  def next_number(number):
    nxt = 0
    str_number = str(number)
    for num in str_number:
      nxt += int(num) ** 2
    return nxt
    
  already_visited = set()
  while n>1:
    if n in already_visited:
      return True
    already_visited.add(n)
    n = next_number(n)
    
  return False

# Solution 2 (Using Modulo)
def is_looping(n):
  def next_number(number):
    nxt = 0
    while number > 0:
      digit = number % 10
      nxt += digit**2
      number = number // 10
    return nxt
  already_visited = set()
  while n>1:
    if n in already_visited:
      return True
    already_visited.add(n)
    n = next_number(n)
    
  return False
    
