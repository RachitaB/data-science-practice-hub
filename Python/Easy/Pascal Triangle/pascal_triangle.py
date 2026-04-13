def generate(numRows):
  
  triangle=[]
  for rn in range(numRows):
	  #initialize with all 1's
	  row = [1] * (rn + 1)
	  #middle value logic
	  for j in range(1,rn):
	    row[j] = triangle[rn-1][j] + triangle[rn-1][j-1]
	  triangle.append(row)
	  
  return triangle
	
    
  
	
