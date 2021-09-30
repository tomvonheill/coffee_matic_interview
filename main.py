from constants import DRINK_LIST
import sys
from ingredients import Ingredient_Inventory,Ingredient
from constants import *
from drinks import Drink_Inventory, Drink, fill_drink_inventory_from_dict

if __name__ == "__main__":
    #set up our inventorys
    ing_inv = Ingredient_Inventory(INGREDIENT_LIST)
    drink_inv =Drink_Inventory()
    fill_drink_inventory_from_dict(drink_inv,ing_inv,DRINK_LIST)
    drink_inv.display_inventory()
    stdin_fileno = sys.stdin
    for line in stdin_fileno:
        line = line.strip()
        if line =='':
            pass
        elif line.lower() == 'q':
            print('Found exit. Terminating the program')
            exit(0)
        elif line.lower() == 'r':
            ing_inv.restock_inventory()
        elif line.isnumeric() and int(line)>=1 and int(line)<=6:
            indx = int(line)-1
            if indx>=0 and indx<=5:
                if drink_inv.drink_in_stock(indx):
                    drink_inv.dispense_drink(indx)
                    print(f'Dispensing: {drink_inv.get_drink_name(indx)}')
                else:
                    print(f'Out of stock: {drink_inv.get_drink_name(indx)}')
        else:
            print(f'Invalid selection: {line}')
        print('Inventory: ')
        ing_inv.display_inventory()
        print('Menu: ')
        drink_inv.display_inventory()



