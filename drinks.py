from ingredients import I_Inventory_Item, Ingredient, ingredient_dict, Ingredient_Inventory
from constants import DRINK_LIST
from typing import Dict, List

class Drink:
    def __init__(self,name, ingredient_quantity:List[tuple]=[]) -> None:
        #ingreidient name, ingredient value
        self.name =name
        self.ingredient_quantity= ingredient_quantity or []
    
    def add_ingredient_and_quantity(self,ingredient:Ingredient,quantity:float):
        self.ingredient_quantity.append((ingredient,quantity))
    
    def get_formatted_cost(self):
        cost = 0
        for ingredient, quantity in self.ingredient_quantity:
            cost += ingredient.get_cost()*quantity
        return '${:,.2f}'.format(cost)
    
    def in_stock(self):
        return all([ingredient.is_quantity_availible(quantity) for ingredient, quantity in self.ingredient_quantity])
    
    def dispense_drink(self):
        [ingedient.use_quantity(quantity) for ingedient,quantity in self.ingredient_quantity] 
    
    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return f'{self.name}, {self.get_formatted_cost()}, {self.in_stock()}'
    def __lt__(self,other):
        return self.__str__()<other.__str__()

class Drink_Inventory:
    def __init__(self, ) -> None:
        self.drink_inv=[]
    
    def add_drink(self, drink:Drink):
        self.drink_inv.append(drink)
        self.drink_inv.sort()
    
    def display_inventory(self):
        for order,drink in enumerate(self.drink_inv, start=1):
            print(f'{order}, {drink}')
    
    def drink_in_stock(self,indx):
        return self.drink_inv[indx].in_stock()
    
    def dispense_drink(self,indx):
        self.drink_inv[indx].dispense_drink()
    def get_drink_name(self,indx):
        return self.drink_inv[indx].get_name()
    


def fill_drink_inventory_from_dict(drink_inventory:Drink_Inventory, ingredient_inventory:Ingredient_Inventory, drink_configs):
    for drink_name,ingredient_name_dict in drink_configs.items():
        new_drink = Drink(drink_name)
        for ingredient_name, units in ingredient_name_dict.items():
            new_drink.add_ingredient_and_quantity(ingredient_inventory.get_ingredient(ingredient_name),units)
        drink_inventory.add_drink(new_drink)