"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main concepts are: encapsulation, abstraction, and polymorphism.

   Encapsulation means that data lives close to its functionality.

   Abstraction means that we can use methods without knowing the information 
   the method uses internally.

   Polymorphism means that it is eas to make different, interchangeable types.


2. What is a class?
    A class is a type of thing. It is a way of organizing and producing objects
    with similar attributes and methods.


3. What is an instance attribute?
    An instance attribute is set directly on the object, as opposed to class 
    attributes which is a piece of data on the class itself.

4. What is a method?
    Methods are functions of objects 

5. What is an instance in object orientation?
    An instance is an individual occurrence of a class.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
   class attributes are a piece of data on the class itself; when you ask for 
   this instance, it finds it on the class. An instance attribute is set directly on the object.

   An example of this is in a class of malls. Every mall has a class attribute of stores. 
   But an instance attribute can have something specific to each store that does not have to be 
   the same as another instance. One store can have an instance attribute 'clothes' while another store has 'shoes'.

"""
# Parts 2 through 5:
# Create your classes and class methods

class Vegetable(object):
    """A class for vegetables"""
    def __init__(self, name, color, flavor):
        self.name = name
        self.color = color
        self.flavor = flavor

    def description(self):
        print "This is a %s %s that tastes %s." % (self.color, self.name, self.flavor)


cucumber = Vegetable("cucumber", "green", "crunchy")

cucumber.description()

class Wintermelon(Vegetable):
    """A vegetable available seasonally"""

    def __init__(self, name, color, flavor):
        super(Vegetable, self).__init__(self, "wintermelon", "white", "crunchy")

class Movies(object):
    """Class describing movie titles, genre, and era"""
    def __init__(self, name, genre, era):
        self.name = name
        self.genre = genre
        self.era = era

    def watched(self):
        """Record whether the movie has been watched."""
        self.watched = True

PowerRangers = Movies("PowerRangers", "action", "current")
PowerRangers.watched()

class Animal(object):
    """A class of animals"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def description(self):
        print "This is a %s named %s." % (self.name, self.species)

class Duck(Animal):
    """subclass of animal"""
    sound = 'quack'

    def __init__(self, name):
        self.name = name
        self.species = "duck"

    def make_sound(self):
        return "The %s goes %s" % (self.species, sound)


