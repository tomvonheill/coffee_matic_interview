(or don't readme lol)
## How to run
python3 main.py will start up the program

### Some Improvements to make

- lets get something to manage stdin
- abstract out some interfaces... seems like we have a lot of overlap between drink/drinks/ingredient.
- looks like drink and ingredient could use the dataclass wrapper.... is it worth it?
- some useless functions on the ingredient_inventory class
- have a class that instantiates drink inventory/ ingredient inventory, this way we may be able to consume other data sources without changing the drink/ingredient class
- maybe look into observer pattern.... this may be fruitless as we are really just dealing with collections at the moment