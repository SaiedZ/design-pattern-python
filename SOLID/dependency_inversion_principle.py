"""
The Dependency Inversion Principle (DIP) is a principle of object-oriented design that states:
1- High-level modules should not depend on low-level modules. Both should depend on abstractions.
2 - Abstractions should not depend on details. Details should depend on abstractions.
"""
from abc import abstractmethod
from enum import Enum


# Example 1



class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass


class Relationships(RelationshipBrowser):  # low-level
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # dependency on a low-level module directly
    # bad because strongly dependent on e.g. storage type

    # def __init__(self, relationships):
    #     # high-level: find all of john's children
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

# low-level module
relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)


# Example 2


"""
In this example, the ReportGenerator class depends on the abstract DataSource
class rather than directly depending on the Database or Filesystem classes.
This allows for flexibility in choosing which data source to use without modifying
the ReportGenerator class. The Database and Filesystem classes both implement
the get_data method from the DataSource abstract class, allowing them to be
used interchangeably as the data source for the ReportGenerator.
This implementation follows the first part of the DIP.

The second part of the DIP is implemented by making sure that the abstract DataSource
class does not depend on any implementation details of the Database or Filesystem
classes. The get_data method in the DataSource abstract class is defined without
any implementation details, leaving it up to the concrete implementations to define
how data is retrieved.
"""

from abc import ABC, abstractmethod

# Define an abstract class for the high-level module to depend on
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

# Define a low-level module that implements the abstract class
class Database(DataSource):
    def get_data(self):
        # code to retrieve data from database
        pass

# Define another low-level module that implements the abstract class
class Filesystem(DataSource):
    def get_data(self):
        # code to retrieve data from filesystem
        pass

# Define a high-level module that depends on the abstract class
class ReportGenerator:
    def __init__(self, data_source: DataSource):
        self.data_source = data_source

    def generate_report(self):
        data = self.data_source.get_data()
        # code to generate report using data
        pass
