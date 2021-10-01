from constants import INGREDIENT_LIST
from ingredients import I_Inventory_Item, Ingredient

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
    
    def add_ingredient_to_inventory(self, ingredient_name:str, ingredient_instance:I_Inventory_Item):
        self.ingredient_inv[ingredient_name]=ingredient_instance
    
    def get_ingredient(self, ingredient_name):
        return self.ingredient_inv.get(ingredient_name)

