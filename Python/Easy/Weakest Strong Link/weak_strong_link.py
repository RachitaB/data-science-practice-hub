def weakest_strong_link(strength):
  m=len(strength) # no of rows
  n=len(strength[0]) # no of columns
  
  min_in_row = [0] * m
  max_in_column = [0] * n
  
  #add min of rows in an array
  for i in range(m):
    min_in_row[i] = min(strength[i])
  
  #add max of columns in an array
  for j in range(n):
    current=0
    for i in range(m):
      current = max(current,strength[i][j])
    max_in_column[j] = current
  
  
  for i in min_in_row:
    for j in max_in_column:
      if i==j:
        return i
  return -1
  
