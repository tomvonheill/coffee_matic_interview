#testing dynamically creating ingredients
from typing import List, Tuple
from constants import INGREDIENT_LIST
from abc import ABC, abstractmethod

class I_Inventory_Item(ABC):
    """
    Interface fo keeping track of an inventory item
    """

    @abstractmethod
    def get_cost(self)->float:
        """Return the cost float/int"""
        raise NotImplementedError
    @abstractmethod
    def is_quantity_availible(self, quantity:int)->bool:
        """Check to see if instance has enough stock"""
        raise NotImplementedError
    @abstractmethod
    def use_quantity(self, quantity:int):
        """Subtract quantity from stock"""
        raise NotImplementedError
    @abstractmethod
    def restock(self):
        """Increase stock quanity"""
        raise NotImplementedError

class Ingredient(I_Inventory_Item):
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
    def use_quantity(self, quantity) -> None:
        self.stock-=quantity
    def restock(self) ->None:
        self.stock =self.init_stock
    def __repr__(self) -> str:
        return f'{self.name}, {self.stock}'
    def __str__(self) -> str:
        return self.__repr__()

class Ingredient_Inventory:
    def __init__(self, ingredient_list:List[Tuple]):
        self.ingredient_inv = {args[0]: Ingredient(*args) for args in ingredient_list}
    
    def display_inventory(self) -> None:
        for name,ingredient in sorted(self.ingredient_inv.items()):
            print(ingredient)
    
    def use_ingredient(self, ingredient_name:str,units:float)->None:
        self.ingredient_inv[ingredient_name].use_quantity(units)
    
    def restock_inventory(self)->None:
        for ingredient in self.ingredient_inv.values():
            ingredient.restock()
    
    def is_ingredient_availible(self, ingredient_name:str,units:float)->None:
        self.ingredient_inv[ingredient_name,units]
    
    def add_ingredient_to_inventory(self, ingredient_name:str, ingredient_instance:I_Inventory_Item)->None:
        self.ingredient_inv[ingredient_name]=ingredient_instance
    
    def get_ingredient(self, ingredient_name)->I_Inventory_Item:
        return self.ingredient_inv.get(ingredient_name)


ingredient_dict = {ingredient_name: Ingredient(ingredient_name,price) for ingredient_name, price in INGREDIENT_LIST}
    
