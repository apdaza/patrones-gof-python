class Expresion:
    def __init__(self, value=None, left=None, right=None):
        self.__value__ = value
        self.__left__ = left
        self.__right__ = right

class ExpresionNumber(Expresion):

    def evaluate(self):
        return int(self.__value__)

class ExpresionPluss(Expresion):

    def evaluate(self):
        return self.__left__.evaluate() + self.__right__.evaluate()
 

class ExpresionMinus(Expresion):

    def evaluate(self):
        return self.__left__.evaluate() - self.__right__.evaluate()