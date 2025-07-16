

class Recipe:
    def __init__(self,
            name: str,
            input:dict[str,float],
            output:dict[str,float],
            productionTime: float,
            gui_Icon:str):
        self.name = name
        self.input = input
        self.output = output
        self.productionTime = productionTime
        self.gui_Icon = gui_Icon
class Machine:
    def __init__(self,
            name: str,
            production_Rate:float,
            required_Power:float,
            gui_Icon:str,
            recipes:Recipe):
        self.name = name
        self.productionRate = production_Rate
        self.requiredPower = required_Power
        self.guiIcon = gui_Icon
        self.recipes = recipes
        

