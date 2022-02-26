# School Catalogue
# Let’s put your knowledge of classes to the test by creating a digital school catalog for the New York City Department of Education. The Department of Education wants the catalog to hold quick reference material for each school in the city.

# We need to create classes for primary and high schools. Because these classes share properties and methods, each will inherit from a parent School class. Our parent and three child classes have the following properties, getters, setters, and methods:

# School
# Properties: name (string), level (one of three strings: 'primary', 'middle', or 'high'), and numberOfStudents (integer)
# Getters: all properties have getters
# Setters: the numberOfStudents property has a setter
# Methods: A __repr__ method that displays information about the school.
# Primary
# Includes everything in the School class, plus one additional property
# Properties: pickupPolicy (string, like "Pickup after 3pm")
# Middle
# Does not include any additional properties or methods
# High
# Includes everything in the School class, plus one additional property
# Properties: sportsTeams (list of strings, like ['basketball', 'tennis'])

class School:
  
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, new_amount):
    self.numberOfStudents = new_amount

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students."




class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_policy(self):
    return self.pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f"   The pickup policy is {self.pickupPolicy}."


mySchool = School("Cocoa Academy", "high", 100)
print(mySchool)
print(mySchool.get_name())
print(mySchool.get_level())
mySchool.set_numberOfStudents(200)
print(mySchool.get_numberOfStudents())

print('\n')

testSchool = PrimarySchool("Cocoa Niblets Academy", 300, "Pickup Allowed")
print(testSchool.get_policy())
print(testSchool)
print('\n')

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, 'high', numberOfStudents)
    self.sportsTeams = sportsTeams

  def getSportsTeams(self):
    return self.sportsTeams
  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + f" Our sports teams are: {', '.join(self.sportsTeams)}."

c = HighSchool("Matcha High", 500, ["Competitive Stirring", "Varsity Measuring"])
print(c.getSportsTeams())
print(c)
