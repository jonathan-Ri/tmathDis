import numpy
from random import randint

#Llenar la matriz con numeros random entre 1 y 9
#Retornar la suma de concentraciones de los bloques extraidos

def inicio(arrayList,p):
  aux2=[]
  x=0

  for j in range(p):
    aux2.insert(j,0)

  aux=arrayList.pop(p-1)
  arrayList.insert(p-1,aux2)

  for i in range(len(aux)):
    x=x+aux[i]


  return x
#esta funcion sirve para botar la ultima fila y guardar su valor


#----------------------------------------------------------------
def count(arrayList,p,q):
  x=0
  for i in range(0,len(arrayList)-1):
    if arrayList[i+1][q]==0:
      x=x+1
      print(x)
  return x
#sirve para contar los ceros en la respectiva columna
#----------------------------------------------------------------
def caer(arrayList,p,q):
  x=0
  if ((arrayList[p][q] <= count(arrayList,p,q)) and (arrayList[p+1][q]==0) ):
    x=arrayList[p][q]
    arrayList[p][q]=0
  return x
#sirve para botar el cuadro en que se encuentra en caso de ser necesario
#----------------------------------------------------------------
p=int(input("Ingrese dimension de la matriz: "))

arrayList = []
for i in range(p):
  s=[]

  for j in range(p):
    s.insert(j,randint(1,2))
  arrayList.insert(i,s)
  
print(arrayList)    
for q in range(p):
  print(arrayList[q])

print("-------------------------------------------")

suma =inicio(arrayList,p)

print(arrayList)

for k in range(len(arrayList)-2,0,-1):
  for l in range(len(arrayList)):
    suma =suma + caer(arrayList,k,l)
    for q in range(p):
      print(arrayList[q])
    print("-------------------------------------------")

for q in range(p):
  print(arrayList[q])
print(suma)
#cuerpo del programa
#------------------------------------------------------------------
  


