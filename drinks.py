from ingredients import I_Inventory_Item, Ingredient_Inventory
from typing import List, Tuple

from abc import ABC, abstractmethod

class I_Composite_Inventory_Item(ABC):
    """Composed of Inventory Items, wraps them and handles them as a composit item"""
    @abstractmethod
    def add_inventory_item_and_quantity(self,ingredient:I_Inventory_Item,quantity:float):
        """Add Inventory Item and specific quanity of that item needed to composite makeup"""
        pass
    
    @abstractmethod
    def in_stock(self)->bool:
        """Checks if inventory items i'm composed of are in stock"""
        pass
    
    @abstractmethod
    def execute_item_creation(self)->None:
        """Will consume inventory items i'm composed of"""
        pass
    @abstractmethod
    def get_formatted_cost(self)->str:
        """returns cost of item string form"""
        pass
    
    @abstractmethod
    def get_name(self) ->str:
        """Return Item Name"""

class Drink(I_Composite_Inventory_Item):
    """Drink is a collection of Inventory Items, wraps their use and aggregates their functions """
    def __init__(self,name:str, ingredient_quantity:List[Tuple[I_Inventory_Item,int]]=[]) -> None:
        self.name =name
        self.ingredient_quantity= ingredient_quantity or []
    
    def add_inventory_item_and_quantity(self,ingredient:I_Inventory_Item,quantity:float):
        """Add Inventory Item and specific quanity of that item needed to composite makeup"""
        self.ingredient_quantity.append((ingredient,quantity))
    
    def get_formatted_cost(self)->str:
        """
        outputs the cost in $dollar.cents format
        """
        cost = 0
        for ingredient, quantity in self.ingredient_quantity:
            cost += ingredient.get_cost()*quantity
        return '${:,.2f}'.format(cost)
    
    def in_stock(self)->bool:
        """
        Checks if all inventory items in the drinks composition have
        sufficient quanity to create the composite item
        """
        return all([ingredient.is_quantity_availible(quantity) for ingredient, quantity in self.ingredient_quantity])
    
    def execute_item_creation(self)->None:
        """Take the quantities away from inventory items this object is composed of"""
        [ingedient.use_quantity(quantity) for ingedient,quantity in self.ingredient_quantity] 
    
    def get_name(self) ->str:
        """Return Item Name"""
        return self.name

    def __str__(self) -> str:
        return f'{self.name}, {self.get_formatted_cost()}, {self.in_stock()}'
    def __lt__(self,other)->bool:
        return self.__str__()<other.__str__()

class Drink_Inventory:
    def __init__(self, ) -> None:
        self.drink_inv=[]
    
    def add_drink(self, drink:Drink)->None:
        self.drink_inv.append(drink)
        self.drink_inv.sort()
    
    def display_inventory(self)->None:
        for order,drink in enumerate(self.drink_inv, start=1):
            print(f'{order}, {drink}')
    
    def drink_in_stock(self,indx)->bool:
        return self.drink_inv[indx].in_stock()
    
    def dispense_drink(self,indx)->None:
        self.drink_inv[indx].execute_item_creation()
    def get_drink_name(self,indx)->str:
        return self.drink_inv[indx].get_name()
    


def fill_drink_inventory_from_dict(drink_inventory:Drink_Inventory, ingredient_inventory:Ingredient_Inventory, drink_configs):
    for drink_name,ingredient_name_dict in drink_configs.items():
        new_drink = Drink(drink_name)
        for ingredient_name, units in ingredient_name_dict.items():
            new_drink.add_inventory_item_and_quantity(ingredient_inventory.get_ingredient(ingredient_name),units)
        drink_inventory.add_drink(new_drink)