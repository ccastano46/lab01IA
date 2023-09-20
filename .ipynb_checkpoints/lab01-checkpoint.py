sucesores = 0
estados = 0

def definicion_estados():
    global sucesores
    global estados
    sucesores = {'S':[['A',3],['D',4]],
                 'A':[['S',3],['D',5],['B',4]],
                 'B':[['E',5],['C',4],['A',4]],
                 'C': [['B',4]],
                 'D': [['A',5],['S',4],['E',2]],
                 'E': [['B',5],['D',2],['F',4]],
                 'F': [['E',4],['G',3]],
                 'G':[['F',3]]}
    estados = [list(sucesores.keys()), [11,10.4,6.7,4.0,8.9,6.9,3.0,0.0]]
def initial():
    return 'S'
def actionResults(estado):
    estado = estado.upper()
    secuencia_sucesores = []
    try:
        for sucesor in sucesores[estado]:
            secuencia_sucesores.append(sucesor[0])
    except KeyError:
        print(estado,"no es un estado valido")
    return secuencia_sucesores

def isGoal(estado):
    estado = estado.upper()
    if not(estado in sucesores.keys()): print(estado, 'no es un estado valido')
    if(estado == 'G'): return True
    else: return False

def actionCost(e1,e2):
    e1 = e1.upper()
    e2 = e2.upper()
    costo = 0
    encontrado = False
    try:
        sucesores_e1 = sucesores[e1]
        sucesores[e2]
        for sucesor in sucesores_e1:
            if (sucesor[0] == e2):
                costo = sucesor[1]
                encontrado = True
                break
        if not(encontrado): print(e2, "no es sucesor de", e1)
    except ValueError:
        print(e1, "o", e2, "no es un estado valido")
    return costo
def heuristicCost(estado):
    try:
        estado = estado.upper()
        return estados[1][estados[0].index(estado)]
    except ValueError:
        print(estado, "no es un estado valido")
        return 0
def menu():
    print('Escoja una de las siguientes opciones:')
    print('1.Conocer el estado inicial')
    print('2.Los sucesores de un estado')
    print('3.Averiguar si cierto estado es el estado objetivo')
    print('4.Conocer el coste de avance de un estado a otro.')
    print('5.Estimar el costo de recorrido de un estado al estado objetivo')
    print('6.Salir')
    op = input('>>')
    if(op == '1'):
        print(initial())
    elif(op == '2'):
        e = input('Indique el estado del cual desea conocer sus sucesores: ')
        print(actionResults(e))
    elif(op == '3'):
        e = input('Indique el estado que desea analizar: ')
        print(isGoal(e))
    elif(op == '4'):
        e1 = input('Indique el estado del cual parte: ')
        e2 = input('Indique el estado al cual desea llegar: ')
        print(actionCost(e1,e2))
    elif(op == '5'):
        e = input('Indique el estado del cual parte: ')
        print("El costo de ir desde", e.upper(), "hasta el estado objetivo puede ser de: ", heuristicCost(e))
    elif(op == '6'):
        print('Hasta pronto')
        exit()
    else:
        print('Opción invalida, intentelo otra vez.')
    menu()

def main():
    definicion_estados()
    menu()
main()