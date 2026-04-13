def triangular_sum(nums):

  while len(nums) > 1:
    newNums=[]
    for i in range(1,len(nums)):
  	  a = (nums[i-1] + nums[i]) % 10
  	  newNums.append(a)
    
    nums=newNums
  return nums[0] 
