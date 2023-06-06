"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    x = open("data.csv", "r").readlines()
    segunda= [int(z[2]) for z in x]
    sol=sum(segunda)
    

    
    return sol


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    x= open("data.csv", "r").readlines()
    primera= [(z[0]) for z in x]
    valores=list(set(primera))
    lista=[(i,len([b for b in primera if b==i])) for i in valores]
    lista.sort(key= lambda x:x[0])
    

    return lista


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    x = open("data.csv", "r").readlines()   
    valores=list(set([z[0] for z in x] ))
    listas= [(z[0], int(z[2])) for z in x]
    listas=[list(i) for i in listas]
    lista=sorted([(i,sum([b[1] for b in listas if b[0]==i])) for i in valores], key=lambda x: x[0])  
    return lista


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """    


    x = open("data.csv", "r").readlines()
    fecha= [z[4:14] for z in x]     
    meses=[ (x[5:7]) for x in fecha]
    valores=list(set(meses))
    lista=[]
    for i in valores: 
        c=[b for b in meses if b==i]        
        c=len(c)        
        lista.append(((i),c))    
    lista.sort(key=lambda x: x[0])

    

    return lista


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    x = open("data.csv", "r").readlines()
    primera= [z[0] for z in x]   
    
    valores=list(set(primera))
    listas= [(z[0], int(z[2])) for z in x]
    listas=[list(i) for i in listas]
     
    lista=[]
    for i in valores: 
        c=[b[1] for b in listas if b[0]==i] 
        lista.append((i,max(c), min(c)))    
    lista.sort(key=lambda x: x[0])

    return lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import re
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x]    
    pattern = r'\s[a-z]{3}.*'
    a=[re.findall(pattern, j) for j in x]    
    a=[x[0].strip() for x in a]
    lista=[]
    for i in a:
        b=i.split(',')
        for k in b:
            lista.append(k)
    lista1=[]    
    listas=[]
    for c in lista: 
        d=c.split(':')
        lista1.append(d[0])
        listas.append([d[0], int(d[1])])
    valores= list(set(lista1))
    valores.sort()
    listota=[]
    for i in valores: 
        c=[b[1] for b in listas if b[0]==i] 
        listota.append((i,min(c), max(c)))    
    return listota


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    x = open("data.csv", "r").readlines()
    segunda= [int(z[2]) for z in x]     
    valores=list(set(segunda))
    valores.sort()
    listas= [(z[0], int(z[2])) for z in x]
    listas=[list(i) for i in listas]
    solucion=[]
    for i in valores: 
        b=[x[0] for x in listas if (x[1])==i]
        solucion.append((i, b))
    return solucion


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    x = open("data.csv", "r").readlines()
    segunda= [int(z[2]) for z in x]     
    valores=list(set(segunda))
    valores.sort()
    listas= [(z[0], int(z[2])) for z in x]
    listas=[list(i) for i in listas]
    solucion=[]
    for i in valores: 
        b=[x[0] for x in listas if (x[1])==i]
        b=list(set(b))
        b.sort()
        solucion.append((i, b))
    return solucion


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import re
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x]    
    pattern = r'\s[a-z]{3}.*'
    a=[re.findall(pattern, j) for j in x]    
    a=[x[0].strip() for x in a]
    lista=[]
    for i in a:
        b=i.split(',')
        for k in b:
            lista.append(k)
    lista1=[]    
    listas=[]
    for c in lista: 
        d=c.split(':')
        lista1.append(d[0])
        listas.append([d[0], int(d[1])])
    valores= list(set(lista1))
    valores.sort()
    listota2=[]
    listota1=[]
    for i in valores: 
        c=[b[1] for b in listas if b[0]==i] 
        listota1.append(i) 
        listota2.append(len(c))   
    dicc= dict(zip(listota1, listota2))
    return dicc


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x]    

    sol= [(i[0],i.count(',')-i.count(':')+2, i.count(':')) for i in x]

    return  sol


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x] 
    x=[z.split() for z in x]  
    x=[(int(z[1]), z[3].split(',')) for z in x] 
    lista=[]
    for i in x:
        lista +=i[1]
    valores=list(set(lista))
    valores.sort()
    cont= []

    for j in valores:
        b=[m[0] for m in x if j in m[1] ]
        
        cont.append(sum(b))
        
    dicc= dict(zip(valores, cont))
    return dicc


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import re
    x = open("data.csv", "r").readlines()
    x = [z.replace("\t", " ") for z in x]
    x = [z.replace("\n", "") for z in x] 
    x=[z.split() for z in x]      
    x=[(z[0], z[4].split(',')) for z in x] 
    primera= [z[0] for z in x]
    segunda=[z[1] for z in x]
    sec=[]
    pattern = r'\d{1,2}'
    for m in segunda: 
        a=[(re.findall(pattern, j)) for j in m] 
        
        sec.append(a)
    num=[]
    for m in sec: 
        f=[int(d[0]) for d in m]
        num.append(sum(f))
    
    valores= list(set(primera))
    valores.sort()

    doble=[[num[i], primera[i]] for i in range(len(primera))]
    sol1=[]
    sol2=[]
    for k in valores: 
        g=[i[0] for i in doble if i[1]==k]
        sol1.append(k); sol2.append(sum(g))

    dicc= dict(zip(sol1, sol2))
    return dicc
    
print(pregunta_12())
