def max_avg_subarray(nums, k):
  ans = float("-inf")
  
  for i in range(len(nums)):
    if(i+k) <= len(nums):
      temp = 0
      for j in range(i,i+k):
        temp += nums[j]
      ans = max(temp,ans)
  return round(ans/k,2)
