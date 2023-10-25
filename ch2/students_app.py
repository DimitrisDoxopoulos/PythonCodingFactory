# Class def

class Student:
    """
    A class that represents a person with firstname and lastname

    Attributes:
    - firstname (str) : the firstname of the person
    - lastname (str) : the lastname of the person
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
def main():
    """
    Makes a student and prints firstname and lastname
    """
    p = Student('Alice', 'Borderland')
    print(p.firstname + " " + p.lastname)

if __name__ == '__main__':
    main()