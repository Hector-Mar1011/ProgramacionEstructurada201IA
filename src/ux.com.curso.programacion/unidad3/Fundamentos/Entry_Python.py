def pregunta_1():
    print(2**3**2)

def pregunta_2():
    x = 10/2
    print(type(x))

"""
x = 1 x = x x == x
"""
def pregunta_3():
    x = 1
    x = x 
    print(x == x )

"""
Orden de operaciones primero evalua // que es
una division entera que no devuelve flotantes y
despues evalua * entonces 1 // 2 es = 0 y = * 3 = 0 
"""
def pregunta_4():
    print(1 // 2 * 3)
"""
Orden de Operadores primero evalua * y posteriormente
evalua +.
"""
def pregunta_5():
    X = 2 + 3 * 5
    print(X)
"""
Al ser string se concatenan
"""
def pregunta_6():
    a = '1'
    b = '2'
    print(a + b)
"""
El operado % devuelve el residuo de la 
división entonces 11 dividido entre 3 es 3 
con un residuo de 2 por lo tanto el resultado es 2
"""
def pregunta_7():
    z = 11 % 3
    print(z)
"""
El operadon // devuelve el cociente de la división entera
"""
def pregunta_8():
    x = 5
    y = 2
    print(x // y )

def pregunta_9():   
    val = 10
    val += 5 * 2
    print(val)
"""
bool("") es false porque una cadena vacia
se considera false.
"""
def pregunta_10():
    print(bool(""), bool(" "), bool(0), bool(0.00))

def main():
    pregunta_1()
    pregunta_2()
    pregunta_3()
    pregunta_4()
    pregunta_5()
    pregunta_6()
    pregunta_7()
    pregunta_8()
    pregunta_9()
    pregunta_10()



if __name__ == "__main__":
    main()

