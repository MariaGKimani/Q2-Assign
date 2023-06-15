#input :length,moral lessons,age group, name,language
#process:
#Determine a class: and its  attributes: Story,Storyteller and Translator
#  Create methods and attributes for each
#Translator inherits from storyteller



class Story:
    def __init__(self, length, moral_lesson, age_group):
        self.length = length
        self.moral_lesson = moral_lesson
        self.age_group = age_group

class StoryTeller(Story):
    def __init__(self, name, language):
        super().__init__("length","moral_lesson","age_group")
        self.name= name
        self.language = language


    def tell_story(self, story):
        print(f"{self.name} is telling a story in {self.language}:")
        

class Translator(StoryTeller):
    def __init__(self, name, language, target_language):
        super().__init__(name, language)
        self.target_language = target_language

    def translate_story(self, story):
        print(f"{self.name} is translating a story from {story.language} to {self.target_language}:")
    


story = Story("Welcome back", "SHHH", "Drink coffee and code", "Hey")
storyteller = StoryTeller("Goretti", "Python")
storyteller.tell_story(story)

translator = Translator("Maria", "Spanish", "French")
translator.translate_story(story)



#question2

#input  ----ingredients,preptime,cookingmethod,nutritional information
#PROCESS --- Determine a class and its attributes
#create a method

class Recipe:
    def __init__(self,name,country,ingredients,preparationTime,cookingMethod,nutritionalInformation):
        self.name = name
        self.country = country
        self.ingredients = ingredients
        self.preparationTime = preparationTime
        self.cookingMethod = cookingMethod
        self.nutritionalInformation = nutritionalInformation
    def display_recipe(self):
        return f"Name:{self.name}\nIngredients:{self.ingredients}\nPreperation Time:{self.preparationTime}"
    

class KikuyuRecipe(Recipe):
    def __init__(self, name, country, ingredients, preparation_time, cooking_method, nutrition_information, spices, serving_suggestion):
        super().__init__(name, country, ingredients, preparation_time, cooking_method, nutrition_information)
        self.spices = spices
        self.serving_suggestion = serving_suggestion

    def print_recipe(self):
        return f"{super().display_recipe()}\nSpice Used:{self.spices}\nServing Suggestion:{self.serving_suggestion}"
      



recipe1 = Recipe("Chocolate Cake","Africa","butter,sugar,flour,eggs","1hour","Oven","Strong")
print(recipe1.display_recipe())

kikuyurecipe1 = KikuyuRecipe("White Rice","Kenya","oil","2hours","Boiling","Strong","BlackPepper","Withpeas")
print(kikuyurecipe1.print_recipe())


#question 3

#input = diet, typical lifespan, migration,patterns,
# = Determine class(Species,Prey,Predator)Determine the attributes of each class
# = Create instances and access their properties through methods


class Species:
    def __init__(self, name, diet, lifespan, migration_pattern):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan
        self.migration_pattern = migration_pattern

class Predator(Species):
    def __init__(self, name, diet, lifespan, migration_pattern, hunting):
        super().__init__(name, diet, lifespan, migration_pattern)
        self.hunting= hunting


class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern, running):
        super().__init__(name, diet, lifespan, migration_pattern)
        self.run = running


species1= Species("cheetah ","meat","20years","done")
predator1 = Predator ("lions", "meat", "25 years ", "seasonal", "yes ")
prey1 = Prey('gazelle', 'grass','4-6 months ', 'yearly',"no")
print (species1.name,species1.lifespan)




# Question5
# input name, price, and quantity
# determine a class and its attrribute
#create methods
# output total value of the products
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value_product(self):
        return self.price * self.quantity
    
product1 = Product("pen",20,95)
product2 = Product("rubber",10,95)
product3 = Product("pencil",15,95)
product4 = Product("book",100,95)
print(product1.total_value_product())

total = product1.total_value_product()+ product2.total_value_product() +product3.total_value_product()+product4.total_value_product()
print(total)


#question6

#input name age grades a list of integers
# determine a class and its attributes
# Create a method to calculate avg grade,
# display studentinfo
#  and determine if the student has passed

class Student:
    def __init__(self, name, age,*grades):
        self.name = name
        self.age = age
        self.grades = list(grades)

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_student_information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def determine_if_passed(self):
        average_grade = sum(self.grades) / len(self.grades)
        if average_grade >= 60:
            return True
        else:
            return False

student1 = Student("Goretti",20, [80, 70, 90])
student2 = Student("Gladys", 22, [50, 60, 70])
student3 = Student("Irene",24,[90,88,95])
print(student1.calculate_average_grade())
print(student1.determine_if_passed())
print(student1.display_student_information())

print(student2.calculate_average_grade())
print(student2.determine_if_passed())
print(student2.display_student_information())








