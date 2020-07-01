def decorador(funcion):
    def operacion():
        print("ejecutando operacion")
        funcion()
    
    return operacion

@decorador
def operacion_externa():
    print("operacion externa")

@decorador
def operacion2():
    print("operacion2")

operacion_externa()
operacion2()