
class Car:
    """
    Car models a car with tires and an engine
    """

    def __init__(self,engine,tires):
        """
        Método de inicializacion
        """
        self.engine = engine
        self.tires =  tires

    def description(self):
        print(f" Un coche con motor {self.engine} y neumáticos {self.tires}")


