def another_one(digits):
  #started from end
	i=len(digits) - 1
	while i>=0 and digits[i]==9:
	  digits[i] = 0
	  i -= 1
	  
	#if non-9 found then just add 1
	if i>=0:
	 digits[i] += 1
	 return digits
	 
	else:
	  #handles cases where all digits are 9
	  return [1] + digits
