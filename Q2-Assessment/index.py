#input :length,moral lessons,age group, name,language
#process:
#Determine a class: and its  attributes: Story,Storyteller and Translator
#  Create methods and attributes for each
#Translator inherits from storyteller





# class Story:
#     def __init__(self,title,length,moral_lessons,age_group):
#         self.title = title
#         self.length_of_story = length
#         self.moral_lessons = moral_lessons
#         self.age_group = age_group

#     def display_story(self):
#         return f"{self.title}"
# class StoryTeller(Story):
#     def __init__(self,story_type,language):
#         self.story_type = story_type
#         self.language = language
#         self.stories = []
#     def narrate_story(self):
#         return f"{self.story_type} is being narrated in {self.language}"
#     def add_story(self):
#         self.stories.append(self.story_type)


# class Translator(Story):
#     def __init__(self,translated_story):
#         super().__init__("title", "length","moral_lessons", "age_group")
#         self.translated = translated_story
#     def translate_story(self):
#         print(f"Translates {self.title} into {self.translated_language}.")


# story = Story("Born a crime",400,"Hardwork",15)
# print (story.display_story())
# teller = StoryTeller("Novel","English")
# print(teller.narrate_story())
# translator = Translator("Born a crime", 400, "Hardwork", 15, "Lapvona")
# translator.translate_story()




#question2

#input  ----ingredients,preptime,cookingmethod,nutritional information
#PROCESS --- Determine a class and its attributes
# create a method

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


# class Species:
#     def __init__(self, name, diet, lifespan, migration_pattern):
#         self.name = name
#         self.diet = diet
#         self.lifespan = lifespan
#         self.migration_pattern = migration_pattern

# class Predator(Species):
#     def __init__(self, name, diet, lifespan, migration_pattern, hunting):
#         super().__init__(name, diet, lifespan, migration_pattern)
#         self.hunting= hunting


# class Prey(Species):
#     def __init__(self, name, diet, lifespan, migration_pattern, running):
#         super().__init__(name, diet, lifespan, migration_pattern)
#         self.run = running


# species1= Species("cheetah ","meat","20years","done")
# predator1 = Predator ("lions", "meat", "25 years ", "seasonal", "yes ")
# prey1 = Prey('gazelle', 'grass','4-6 months ', 'yearly',"no")
# print (species1.name,species1.lifespan)




# Question5
# input name, price, and quantity
# determine a class and its attrribute
#create methods
# output total value of the products
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value_product(self):
#         return self.price * self.quantity
    
# product1 = Product("pen",20,95)
# product2 = Product("rubber",10,95)
# product3 = Product("pencil",15,95)
# product4 = Product("book",100,95)
# print(product1.total_value_product())

# total = product1.total_value_product()+ product2.total_value_product() +product3.total_value_product()+product4.total_value_product()
# print(total)


#question6

#input name age grades a list of integers
# determine a class and its attributes
# Create a method to calculate avg grade,
# display studentinfo
#  and determine if the student has passed

# class Student:
#     def __init__(self, name, age,*grades):
#         self.name = name
#         self.age = age
#         self.grades = list(grades)

#     def calculate_average_grade(self):
#         return sum(self.grades) / len(self.grades)

#     def display_student_information(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Grades: {self.grades}")

#     def determine_if_passed(self):
#         average_grade = sum(self.grades) / len(self.grades)
#         if average_grade >= 60:
#             return True
#         else:
#             return False

# student1 = Student("Goretti",20, [80, 70, 90])
# student2 = Student("Gladys", 22, [50, 60, 70])
# student3 = Student("Irene",24,[90,88,95])
# print(student1.calculate_average_grade())
# print(student1.determine_if_passed())
# print(student1.display_student_information())

# print(student2.calculate_average_grade())
# print(student2.determine_if_passed())
# print(student2.display_student_information())








class FlightBooking:

    def __init__(self):
        self.flights = []

    def search_flights(self, destination, date):
        for flight in self.flights:
            if flight.destination == destination and flight.date == date:
                return flight

    def reserve_seat(self, flight, passenger_name, passenger_email):
        if flight not in self.flights:
            raise ValueError("Flight not found")

        if passenger_name is None or passenger_email is None:
            raise ValueError("Passenger information not complete")

        flight.passengers.append({
            "name": passenger_name,
            "email": passenger_email,
        })

    def manage_passenger_information(self, flight, passenger_name, field, value):
        for passenger in flight.passengers:
            if passenger["name"] == passenger_name:
                if field == "name":
                    passenger["name"] = value
                elif field == "email":
                    passenger["email"] = value
                else:
                    raise ValueError("Invalid field")

    def generate_booking_confirmation(self, flight):
        confirmation = {
            "flight": flight.id,
            "passengers": flight.passengers,
        }

        return confirmation



