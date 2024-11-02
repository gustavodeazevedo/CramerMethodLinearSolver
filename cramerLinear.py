#SOLUÇÃO DE SISTEMA LINEAR POR CRAMER

import numpy as np

# Definir a matriz dos coeficientes
A= np.array([[1,2,-1],[2,3,1],[5,3,-2]])

# Definir o vetor dos termos independentes
B= np.array([8,1,-11])

# Definir a matriz Ax (trocar coluna x pelo termo indep)
Ax = np.array([[8,2,-1],[1,3,1],[-11,3,-2]])

# calcular os determinante de A e Ax

detA = np.linalg.det(A)
detAx = np.linalg.det(Ax)

# Analisar a solucao pelo determinante

if detA !=0 :
  x = np.linalg.solve(A,B)
  print(f'Sistema Possivel e Determinado : {x}')
else:
  if detA == 0 and detAx == 0 :
    print('Sistema Possivel e Indeterminado ')
  else:
    print('Sistema Impossivel')