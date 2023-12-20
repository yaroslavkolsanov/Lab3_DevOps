import numpy as np 
import tabulate 
 
a = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
 
print('Степень:', 1) 
print(tabulate.tabulate(a)) 
 
for i in range(1,10): 
  print('Степень:', i+1) 
  print(tabulate.tabulate(a.dot(a)))
