from abc import ABC, abstractmethod

class Computer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect_to_projector(self):
        pass

class Notebook(Computer):
    def connect_to_projector(self):
        pass


class Projector(Notebook):
    def connect(self):
        ob1 = Notebook('Asus')
        if isinstance(ob1, Notebook) == True:
            Notebook.connect_to_projector(self)
            return f'Projector connected to {ob1.name}'
        else:
            return f'Error!'

projector = Projector('Projector')
print(projector.connect())
