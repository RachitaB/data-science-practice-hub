def total_letters(N):
  def get_word(number):
    res=""
    units = {
        0: 'zero',1: 'one', 2: 'two', 3: 'three', 4: 'four',
        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 
        9: 'nine',10: 'ten', 11: 'eleven', 12: 'twelve', 
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 
        19: 'nineteen',20: 'twenty', 30: 'thirty', 
        40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 
        80: 'eighty', 90: 'ninety'
    }
    
    # logic for converting numbers here.
    if number >=1000:
      res+= units[number//1000] +"thousand"
      number %= 1000
    
    if number >=100 and number<1000:
      res+= units[number//100] +"hundred"
      number %= 100
      
    if number > 0 and res != "":
      res += "and"
      
    if number >= 20 and number<100:
      res += units[number // 10 * 10]
      number %= 10
      
    if number > 0 and number < 20:
      res += units[number]
      
    return res

  ans = 0
  for num in range(1, N + 1):
    ans += len(get_word(num))
  
  return ans
  
  
	  
