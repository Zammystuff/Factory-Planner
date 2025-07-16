import factory_planner.classes
from  factory_planner.classes import Recipe
##"material will likely be its on class down the line. placeholder for now,same with outputs "
classes = factory_planner.classes




##Defines all bar recipes.
r_ironBar = classes.Recipe("Iron bar",
                           "materialIn",
                           "materialOut",
                           1.00,
                           "file/dir/placeholder")


r_copperBar = classes.Recipe("Copper bar",
                             "materialIn",
                             "materialOut",
                             1.00,
                             "file/dir/placeholder")
