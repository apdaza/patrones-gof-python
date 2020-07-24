class Command:
    def execute(self, recivier):
        pass

class Recivier():
    def show_message(self, msg):
        print(msg)

class DomesticEngineer(Command):
    def execute(self, recivier):
        recivier.show_message("take out the trash")

class Politician(Command):
    def execute(self, recivier):
        recivier.show_message("take the money from the rich, take the votes from poor")

class Programmer(Command):
    def execute(self, recivier):
        recivier.show_message("sell the bugs, charge extra for the fixes")