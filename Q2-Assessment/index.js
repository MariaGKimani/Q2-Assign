class Story {
    constructor(content, length, moralLesson, ageGroup) {
      this.content = content;
      this.length = length;
      this.moralLesson = moralLesson;
      this.ageGroup = ageGroup;
    }
  }
  
  class StoryTeller {
    constructor(name, language) {
      this.name = name;
      this.language = language;
    }
  
    tellStory(story) {
      console.log(`${this.name} is telling a story in ${this.language}:`);
      console.log(story.content);
    }
  }
  
  class Translator extends StoryTeller {
    constructor(name, language, targetLanguage) {
      super(name, language);
      this.targetLanguage = targetLanguage;
    }
  
    translateStory(story) {
      console.log(`${this.name} is translating a story from ${story.language} to ${this.targetLanguage}:`);
      // Translation logic goes here
    }
  }
  
  // Example usage:
  const story = new Story("Once upon a time...", "long", "Always be kind", "children");
  const storyteller = new StoryTeller("John", "English");
  storyteller.tellStory(story);
  
  const translator = new Translator("Maria", "Spanish", "French");
  translator.translateStory(story);
  