def k_radius_avg(nums, k):
  k_rad = [] 
  for i in range(len(nums)):
    if i-k >= 0 and i+k<len(nums):
      temp = 0
      div = 0
      for j in range(i-k,i+k+1):
        temp += nums[j]
        div += 1
      temp = temp / div
      k_rad.append(round(temp,2))
    else:
      k_rad.append(-1)
  return k_rad
