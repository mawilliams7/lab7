def edit_distance(str1, str2):
  """
  Finds the edit distance between two strings.
  
  Args:
    str1: A string
    str2: A string
  
  Returns:
    matrix[len(str1)][len(str2)]: The edit distance between two strings
  """
  matrix = list()
  for i in range(len(str1) + 1):
    row = [0] * (len(str2) + 1)
    matrix.append(row)
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      if i == 0:
        matrix[i][j] = j
      elif j == 0:
        matrix[i][j] = i
      else:
        if str1[i-1] == str2[j-1]:
          matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1],
                              matrix[i][j-1])
        else: 
          matrix[i][j] = min(matrix[i-1][j], matrix[i-1][j-1],
                              matrix[i][j-1]) + 1
  return matrix[len(str1)][len(str2)]

