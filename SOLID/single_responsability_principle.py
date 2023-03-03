"""
The Single Responsibility Principle (SRP) is a principle of
object-oriented design that states that a class should have
only one reason to change. In other words, a class should have
only one responsibility and should not be responsible for more
than one thing. This helps to make the class easier to understand,
modify, and maintain, as well as promoting good design practices
such as modularity and separation of concerns. By adhering to
the SRP, developers can create more robust and maintainable code
that is easier to extend and refactor over tim
"""

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP

    # def save(self, filename):
    #     file = open(filename, "w")
    #     file.write(str(self))
    #     file.close()

    # def load(self, filename):
    #     pass

    # def load_from_web(self, uri):
    #     pass


class PersistenceManager:

    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
