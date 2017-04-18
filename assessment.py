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

class Student(object):
  """ Class to store student data"""
  def __init__(self, first_name, last_name, address)
    self.first_name = first_name
    self.last_name = last_name
    self.address = address

  def __repr__(self):
    return "%s %s lives at %s" % (self.first_name, self.last_name, self.address)

class Question(object):
  """Class for storing question and answers"""
  def __init__(self, question, answer):
    self.question = question
    self.answer = answer

  def __repr__(self):
      """ Returns question and answer)."""

      return "Question: {} \n Answer: {}".format(self.question,
          self.answer)

  def ask_and_evaluate(self):
      """ Prints question, prompts user for answer, then True if correct or False."""

      print self.question
      user_answer = raw_input("> ")
      if user_answer == self.answer:
          return True
      else:
          return False

class Exam(object):
  """Class for exam questions"""
  def __init__(self, name, question):
    self.name = name
    self.question = []

  def __repr__(self):
    return "This is the {} Exam, followed by the question: \n{}".format(self.name, self.question)

  def add_question(self, questions, correct_answer):
    """Adds question and correct answer to create another question"""
    self.question.append(Question(question, correct_answer))

  def administer(self):
      """Ask questions and return score of how many were correct"""

      for question in self.question:
          if question.ask_and_evaluate():
              correct_answer += 1
      # return correct answer divided by total number of questions * 100 to get score
      score = (correct_answer / len(self.question)) * 100
      return score

class StudentExam(object):









