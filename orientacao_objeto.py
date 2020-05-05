'''
O objetivo dessa classe é receber três valores, que formam as dimensões de um paralelepipedo.
Note que, apesar de usarmos getters e setters aqui, ambos servem para aplicações bastante especificas,
i.e. quando é necessário rodar um código ao obter/setar um atributo. O usual no python, todavia, é acessar
o atributo diretamente.
'''

class Paralelepipedo(object):

    def __init__(self, x, y, z): #construtor
        self._x = x
        self._y = y
        self._z = z
    
    @property #getter do x
    def x(self):
        return self._x
    
    @x.setter #setter do y
    def x(self, x):
        self._x = x
    
    ## Todos os códigos abaixo são análogos ao acima, com os getters e setters
    
    @property
    def y(self):
        return self._x
    
    @y.setter
    def y(self, y):
        self._y = y
    
    @property
    def z(self):
        return self._z
    
    @z.setter
    def z(self, z):
        self._z = z
    
    def get_volume(self): #função que retorna o volume do cubo criado
        return self.x * self.y * self.z

obj = Paralelepipedo(10, 10, 10) #aqui, inicializamos um cubo comum, de lado 10; note que a unidade é arbitrária
print("Objeto inicial:", obj.__dict__)
print("Volume do objeto inicial:", obj.get_volume())

# Podemos, todavia, distorcer nosso cubo usando os setters
obj.x = 5
# E, agora, temos:
print("Objeto distorcido:", obj.__dict__)
print("Volume do objeto distorcido:", obj.get_volume())

# Por fim, é possível ler uma propriedade específica utilizando o getter
print("O valor da dimensão y do paralelepipedo é:", obj.y)