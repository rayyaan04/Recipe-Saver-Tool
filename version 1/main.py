


# define recipe class 
class Recipe:
    def __init__(self, name, servings=None, caloriesPS= None, proteinPS= None, carbsPS= None, fatsPS= None, steps = None, ingredients= None, tags= None, notes=""):
        self.name = name
        self.servings = servings
        self.caloriesPS = caloriesPS
        self.proteinPS = proteinPS
        self.carbsPS = carbsPS
        self.fatsPS = fatsPS
        self.steps = steps if steps is not None else []
        self.ingredients = ingredients if ingredients is not None else []
        self.tags = tags if tags is not None else []
        self.notes = notes

# define file handler functions
# load/create recipes.json
def fileLoad():
     pass

# write to recipes.json
def fileWrite():
    pass
    
# user input
def addRecipe():
    answers = {}
    answers["steps"] = input("Input the list of steps for recipe:")
        #add function to seperate each line to object in list
    answers["steps"] = answers["steps"].split()
    print(answers["steps"])
    answers["name"] = input("Name of recipe: ").strip()
    answers["servings"] = int(input("Input no. of servings: "))
    answers["caloriesPS"] = float(input("Input no. of calories per serving: "))
    answers["proteinPS"] = float(input("Input no. of protein per serving: "))
    answers["carbsPS"] = float(input("Input no. of carbs per serving: "))
    answers["fatsPS"] = float(input("Input no. of fats per serving: "))
    answers["steps"] = input("Input the list of steps for recipe:")
    #add function to seperate each line to object in list
    answers["steps"] = answers["steps"].split()
    print(answers["steps"])
    answers["ingredients"] = input("Input the list of ingredients for recipe:")
    #add function to seperate each line to object in list
    
        
    answers["tags"] = input("input the tags, seperated by a ,: ")
    answers["tags" ]= answers["tags"].split(',') # splits each tag into an individual object in a list
    answers["notes"] = input("input any notes: ")
    
    newRecipe = Recipe(**answers)
    
def main():
    answers = {}
    answers["tags"] = input("input the tags, seperated by a ,: ")
    answers["tags" ]= answers["tags"].split(',')
    print(answers["tags"])
main()