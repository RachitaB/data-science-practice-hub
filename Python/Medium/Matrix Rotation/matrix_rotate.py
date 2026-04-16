# Solution
def find_rotation(mat, target):
  def rotate_matrix(mat):
    for i in range(len(mat)):
      for j in range(i+1,len(mat)):
        mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
    
    for i in range(len(mat)):
      mat[i].reverse()
    return mat
  
  for k in range(4):
    if mat == target:
      return True
    mat = rotate_matrix(mat)
      
  return False
