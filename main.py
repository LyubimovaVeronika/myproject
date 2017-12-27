#coding: utf-8
"""
Типы строя
"""
class Culture:
    """
    Культура
    """
    def __repr__(self):
        return self.__str__()

class Democracy(Culture):
    def __str__(self):
        return 'Democracy'

class Dictatorship(Culture):
    def __str__(self):
        return 'Dictatorship'

"""
Само правительство
"""
class Government:
    culture = ''
    def __str__(self):
        return self.culture.__str__()

    def set_culture(self):
        """
        Задать строй правительству : это и есть наш Фабричный Метод
        """
        raise AttributeError('Not Implemented Culture')

"""
Правительство 1
"""
class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()

"""
Правительство 2
"""
class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatorship()

g1 = GovernmentA()
g1.set_culture()
print (str(g1))

g2 = GovernmentB()
g2.set_culture()
print (str(g2))

""" У нас есть класс Правительство. __str__ - метод для получения строкового представления объекта. У класса есть 
абстрактный метод set_culture, позволяющий задать строй правительству. В последствии для дочерних классов Правительства он будет 
переопределяться. Этот метод возвращает дочерний класс класса культуры. Фабричный метод заключается в выстраивании четкой иерархии
классов, но главное, что он позволяет в любой момент расширить структуру классов, потому что в родительском классе уже определен 
набор абстрактных методов. Каждый новый случай требует создания дочернего класса"""