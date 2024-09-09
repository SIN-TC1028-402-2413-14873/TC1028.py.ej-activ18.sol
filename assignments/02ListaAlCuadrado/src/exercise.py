def cuentaPares(m):
    lista = []

    for row in range(len(m)):
        cp = 0
        for column in range(len(m[row])):
            if m[row][column] % 2 == 0:
                cp = cp + 1
        lista.append(cp)
    return lista

def main():

    n = int(input(">>>"))
    m = int(input(">>>"))

    matriz = []
    for row in range(n):
        renglon=[]
        for column in range(m):
            dato = int(input(">>>"))
            renglon.append(dato)
        matriz.append(renglon)
    print(matriz)
    print(cuentaPares(matriz))

if __name__=='__main__':
    main()
