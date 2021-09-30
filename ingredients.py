#testing dynamically creating ingredients
from constants import INGREDIENT_LIST
from abc import ABC, abstractmethod

class I_Ingredient(ABC):

    @abstractmethod
    def get_cost(self):
        raise NotImplementedError
    @abstractmethod
    def is_quantity_availible(self):
        raise NotImplementedError
    @abstractmethod
    def use_quantity(self):
        raise NotImplementedError
    @abstractmethod
    def restock(self):
        raise NotImplementedError

class Ingredient(I_Ingredient):
    def __init__(self, name, cost, init_stock =10) -> None:
        #if its a new ingredient start its stock off
        self.init_stock = init_stock
        self.stock =init_stock
        self.name = name
        self.cost = cost
    def get_cost(self) ->float:
        return self.cost
    def is_quantity_availible(self, quantity)->bool:
        if quantity<= self.stock:
            return True
        return False
    def use_quantity(self, quantity):
        self.stock-=quantity
    def restock(self):
        self.stock =self.init_stock
    def __repr__(self) -> str:
        return f'{self.name}, {self.stock}'
    def __str__(self) -> str:
        return self.__repr__()

class Ingredient_Inventory:
    def __init__(self, ingredient_list:list):
        self.ingredient_inv = {args[0]: Ingredient(*args) for args in ingredient_list}
    
    def display_inventory(self):
        for name,ingredient in sorted(self.ingredient_inv.items()):
            print(ingredient)
    
    def use_ingredient(self, ingredient_name:str,units:float):
        self.ingredient_inv[ingredient_name].use_quantity(units)
    
    def restock_inventory(self):
        for ingredient in self.ingredient_inv.values():
            ingredient.restock()
    
    def is_ingredient_availible(self, ingredient_name:str,units:float):
        self.ingredient_inv[ingredient_name,units]
    
    def add_ingredient_to_inventory(self, ingredient_name:str, ingredient_instance:I_Ingredient):
        self.ingredient_inv[ingredient_name]=ingredient_instance
    
    def get_ingredient(self, ingredient_name):
        return self.ingredient_inv.get(ingredient_name)


ingredient_dict = {ingredient_name: Ingredient(ingredient_name,price) for ingredient_name, price in INGREDIENT_LIST}
    
