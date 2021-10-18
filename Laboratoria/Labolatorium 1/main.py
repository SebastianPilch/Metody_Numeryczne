
import numpy as np
import math
import scipy


def cylinder_area(r :float ,h :float):
    if type(r) is not float or type(h) is not float:
        return np.NaN
    elif r < 0 or h < 0:
        return np.NaN
    else:
        area:float = 2 * math.pi * r * (h + r)
        return area
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """

"""Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
Szczegółowy opis w zadaniu 3.

Parameters:
n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
(x>=1 and x>= 4)
Returns:
np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
"""
def fib(n: int):
    result=[1, 1]
    np.ndarray(result)
    if n <= 0 or type(n) is float:
        return None
    if n==1:
        return [1]
    else:
        result += [result[-1] + result[-2]]
        return result


"""Funkcja zwraca wartości obliczeń na macierzy stworzonej

   na podstawie parametru a.  
   Szczegółowy opis w zadaniu 4.

   Parameters:
   a (float): wartość liczbowa 

   Returns:
   touple: krotka zawierająca wyniki obliczeń 
   (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
   """

def matrix_calculations(a: float):
    matrix =np.array ([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    det_matrix = scipy.linalg.det(matrix)
    t_matrix = np.transpose(matrix)
    if det_matrix != 0:
        inv_matrix=scipy.linalg.inv(matrix)
    else:
        inv_matrix = np.NaN

    return inv_matrix, t_matrix, det_matrix


"""Funkcja zwraca macierz o wymiarze mxn zgodnie 
z opisem zadania 7.  

Parameters:
m (int): ilość wierszy macierzy
n (int): ilość kolumn macierzy  

Returns:
np.ndarray: macierz zgodna z opisem z zadania 7.
"""
#Zadanie 6
def custom_matrix(m: int, n: int):
    if type(m) is not int or type(n) is not int:
        return None
    else:
        return np.zeros([m, n])


