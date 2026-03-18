def is_same_stripes(matrix):
	daigonal_elements ={}
	
	for i in range(len(matrix)):
	  for j in range(len(matrix[i])):
	    if i-j in daigonal_elements and daigonal_elements[i-j] != matrix[i][j]:
	      return False
	    else:
	      daigonal_elements[i-j] = matrix[i][j]
	
	return True
   
