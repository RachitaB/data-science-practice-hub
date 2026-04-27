def spiral_order(matrix):
  left,right = 0, len(matrix[0]) -1 
  top,bottom = 0, len(matrix) -1

  spiral_mat = []
  while left <= right and top <= bottom:
    
    for i in range(left,right+1):
      spiral_mat.append(matrix[top][i])
    top += 1
    
    for i in range(top,bottom+1):
      spiral_mat.append(matrix[i][right])
    right -= 1
    
    if not (left<=right and top<=bottom):
      break
    
    for i in range(right,left-1,-1):
      spiral_mat.append(matrix[bottom][i])
    bottom -= 1
    
    for i in range(bottom,top-1,-1):
      spiral_mat.append(matrix[i][left])
    left +=1 
  
  return spiral_mat
