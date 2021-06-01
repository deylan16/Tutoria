def semi(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    if filas >=2:
        if semi_sumafila(matriz,0,0,filas,columnas) == semi_sumafila(matriz,1,0,filas,columnas):
            return semi(matriz[1:])
        else:
            return False
    else:
        return True
    
    
def semi_sumafila(matriz,m,n,filas,columnas):
    if n >= columnas:
        return 0
    else:
        return matriz[m][n] + semi_sumafila(matriz,m,n+1,filas,columnas)
    
        





























def semi2(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return semi_aux2(matriz,0,0,filas,columnas)

def semi_aux2(matriz,m,n,filas,columnas):
    if m >= filas:
        return []
    elif n< columnas:
        if matriz[0][1] == 0:
            return [[m,n]] + semi_aux2(matriz,m,n+1,filas,columnas)
        else:
            return  semi_aux2(matriz,m,n+1,filas,columnas)
    else:
        return semi_aux2(matriz,m+1,0,filas,columnas)






























