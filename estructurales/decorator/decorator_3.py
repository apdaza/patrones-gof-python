class Decorator(object):
  """Clase de decorador simple."""
  def __init__(self, func):
    self.func = func

  def __call__(self, *args, **kwargs):
    print('Antes de ser llamada la función.')
    retorno = self.func(*args, **kwargs)
    print('Despues de ser llamada la función.')
    print(retorno)
    return retorno

@Decorator
def function():
  print('Dentro de la función.')
  return "Retorno"

function()