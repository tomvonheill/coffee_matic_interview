## How to run
python3 main.py will start up the program

### Purpose of this readme
The purpose of this readme is to keep track of design descisions, and potential improvements. 

### Some Improvements to make/thoughts (read for thought process)

- lets get something to manage stdin
- abstract out some interfaces... seems like we have a lot of overlap between drink/drinks/ingredient.
- looks like drink and ingredient could use the dataclass wrapper.... is it worth it?
- some useless functions on the ingredient_inventory class
- have a class that instantiates drink inventory/ ingredient inventory, this way we may be able to consume other data sources without changing the drink/ingredient class
- maybe look into observer pattern.... this may be fruitless as we are really just dealing with collections at the moment
- if you have time add some tests
- Looks like Drink may be able to be abstracted out to an inventory_item collection that would wrap the functionality of the inventory item and provide a facade of dealing with the inventory
- get formatted cost seems as though it is taking away from re-usability of the Drink class which could most likely be turned into a Inventory_Item_Composite class/interface.... This could be extended to other uses.... how many interfaces should we split this up into
- move formatting cost way from drink class? or keep it and change to cost_str? could be changed depending on what currency we are using in the future
- clean up tomorrow morning potentially, we are still instantiating ingredient_inventory via Ingredient, really should pass a class to instantiation of type I_Inventory_Item and pass the args from there. Update names put create some folders containint base abstract class and then associated classes.