// class Story {
//   constructor(title, length, moral_lessons, age_group) {
//     this.title = title;
//     this.length_of_story = length;
//     this.moral_lessons = moral_lessons;
//     this.age_group = age_group;
//   }

//   displayStory() {
//     return this.title;
//   }
// }

// class StoryTeller extends Story {
//   constructor(language) {
//     super();
//     this.language = language;
//     this.stories = [];
//   }

//   narrate_story() {
//     return `${this.story_type} is being narrated in ${this.language}`;
//   }

//   add_story() {
//     this.stories.push(this.story_type);
//   }
// }

// class Translator extends Story {
//   constructor(title, length, moral_lessons, age_group, translated_story) {
//     super(title, length, moral_lessons, age_group);
//     this.translated = translated_story;
//   }

//   translate_story() {
//     console.log(`Translates ${this.title} into ${this.translated}.`);
//   }
// }

// const story = new Story("Born a crime", 400, "Hardwork", 15);
// console.log(story.displayStory());

// const teller = new StoryTeller("Novel", "English");
// console.log(teller.narrate_story());

// const translator = new Translator("Born a crime", 400, "Hardwork", 15, "Lapvona");
// translator.translate_story();

// **Ancestral Stories:** In many African cultures, the art of storytelling is passed
// down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.

class  Story{
  constructor (length,morallesson,nameOfTheBook,numberOfPages,authorName,ageGroup){
    this.length = length
    this.morallesson = morallesson
    this.nameOfTheBook = nameOfTheBook
    this.ageGroup = ageGroup
    this.pagesNumber = numberOfPages
    this.authorName = authorName
  }
  displayStory() {
    return(`${this.length}, ${this.morallesson}`); 
  }
}

 let story1 =  new Story(200,"kind","Originals",900,"Allan",30)
 console.log(story1.displayStory());


class StoryTeller extends Story{
  constructor (length,morallesson,nameOfTheBook,numberOfPages,authorName,ageGroup) {
    super(length,morallesson,nameOfTheBook,numberOfPages,authorName,ageGroup);
  }
  displayStoryteller(){
    return (`${super.displayStory()}, ${this.gender}`)
    
  }
}
 let storyteller1 =  new StoryTeller(30,"be original","original",800,"Allan",20)
 console.log(storyteller1.displayStoryteller());

// class Recipe{
//   constructor (uniqueIngredients,preparationTime,cookingmethod,nutritionalInformation){
//     this.prepTime= preparationTime 
//     this.cookingmethod = cookingmethod
//     this.infoNutrition = nutritionalInformation
//     this.ingredients = []
//   }
//   addingredients(){
//     if(!this.ingredients.includes('onions')){
//     this.ingredients.push('onions')
//      return `${this.ingredients}`
//     }else{
//       throw ('You cant add the same ingredient twice')
//     }
//   }
//   nutrition(){
//     return `${this.infoNutrition}`
//   }
// }
// class Morrocan extends Recipe {
//   constructor (uniqueIngredients,preparationTime,cookingmethod,nutritionalInformation){
//     super(uniqueIngredients,preparationTime,cookingmethod,nutritionalInformation)
//     this.ingredients =[];
    
//   }
// }

// let recipe1 = new  Morrocan("Fermented wheat","12 min","Baking",['onions'],"vitamin");
// console.log(recipe1.addingredients());





// QUESTION 7 
class Flights{
  constructor(destination,dates,flights){
    this._destinations=[];
  }
}