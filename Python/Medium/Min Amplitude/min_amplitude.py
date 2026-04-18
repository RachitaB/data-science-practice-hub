def min_amplitude(arr):
  
  if len(arr) < 5:
    return 0
    
  arr.sort()
  #case 1 remove first 3 arr elements
  val1 = arr[-1] - arr[3]  
  #case2 remove first 2 and last element
  val2 = arr[-2] - arr[2]
  #case3 remove first and last 2 elements
  val3 = arr[-3] - arr[1]
  #case4 remove last 3 elements
  val4 = arr[-4] - arr[0]
  
  ans = min(val1,val2,val3,val4)
  
  return ans
