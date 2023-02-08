import math

def area_rectangulo(
    x:float
    ,y:float
): 

    ''' 
    Funcion que calcula el area de un rectangulo

    ---params---
    - x (float): es la base del rectangulo
    - y (float): es la altura del rectangulo

    ---return---
    - area (float): es el area del rectangulo
    '''
    area = x*y
    return area

def distancia_entre_dos_puntos(
    x_1:float,
    x_2:float,
    y_1:float,
    y_2:float
) ->float:
    '''
    Funcion para calcular la distancia entre dos puntos

    ---params---
    - x_1 (float): punto inicial de la base
    - x_2 (float): punto final de la base
    - y_1 (float): punto inicial de la altura
    - y_2 (float): punto final de la altura

    ---return---
    - d (float): distancia entre 2 puntos
    '''
    x = math.pow(x_2-x_1,2)
    y = math.pow(y_2-y_1,2)
    d = math.sqrt(x+y)
    return d