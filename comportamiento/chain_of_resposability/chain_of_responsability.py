class Handler:
    def __init__(self):
        self.__succesor__ = None

    def set_succesor(self, succesor):
        self.__succesor__ = succesor

    def handler_request(self, opt):
        pass


class HandlerOptionOne(Handler):

    def handler_request(self, opt):
        if opt == 1:
            print("Domingo")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionTwo(Handler):

    def handler_request(self, opt):
        if opt == 2:
            print("Lunes")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionThree(Handler):

    def handler_request(self, opt):
        if opt == 3:
            print("Martes")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionFour(Handler):

    def handler_request(self, opt):
        if opt == 4:
            print("Miercoles")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionFive(Handler):

    def handler_request(self, opt):
        if opt == 5:
            print("Jueves")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionSix(Handler):

    def handler_request(self, opt):
        if opt == 6:
            print("Viernes")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionSeven(Handler):

    def handler_request(self, opt):
        if opt == 7:
            print("Sabado")
        else:
            self.__succesor__.handler_request(opt)

class HandlerOptionDefault(Handler):

    def handler_request(self, opt):
        print("Opción no valida")