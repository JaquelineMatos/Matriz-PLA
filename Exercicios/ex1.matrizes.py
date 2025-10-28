def show()
def sumMatrix()
def subMatrix()
def multiplyMatrix() 



print("dadas as matrizes a,b,c calcule [a+(b-ct]*b)")
print()
a = [[2,1], [-3,4]]
b = [[0,-1], [2,5]]
c = [[3,0], [6,1]]
print(f"{'matriz a:':^18}")
show(a)
print(f"{'matriz b:':^18}")
show(b)
print(f"{'matriz b:':^18}")
show(c)

cT = transposedtMatriz(c)
print("resultado 1 (b -ct))")
aux = submatrix(b, ct)
show(aux)
print("resultado 2 (a+(b-ct))")
aux2=sumMatrix(a, aux)
show(aux2)
print("O resultado é")
result=multiplyMatrix(aux, b)
show(result)

