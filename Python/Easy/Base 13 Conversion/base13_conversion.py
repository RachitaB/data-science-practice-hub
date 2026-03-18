def convertToBase13(num):
  base13_digits = "0123456789ABC"
  base13_result = ""
  
  if num==0:
    return "0"
  
  positve_num = abs(num)
  
  while positve_num>0:
    rem=positve_num%13
    base13_digit=base13_digits[rem]
    base13_result = base13_digit + base13_result
    positve_num=positve_num//13
  
  if num<0:
    return "-" + base13_result
  else:
    return base13_result
