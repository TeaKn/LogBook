from enum import Enum

from ServiceLayer.model import Subject

def input_choice(options):
    """
    Lists options.
    """
    options = list(options)
    for i, option in enumerate(options, 1):
        print(f'{i}) {option}')
    choice = None
    while True:
        try:
            choice = int(input('> ')) - 1
            return options[choice]
        except (ValueError, IndexError):
            print("Wrong input. Try again.")

class Menu(Enum):
    """
    Class for choice in menu.
    """
    def __init__(self, functionality_name, functionality):
        """
        Constructor.
        """
        self.functionality_name = functionality_name
        self.functionality = functionality

    def __str__(self):
        """
        Converts the enum to string.
        """
        return self.functionality_name

def add_subject():
    """
    Adds subject.
    """
    name = input('Name of subject: ')
    subject = Subject(name)
    subject.persist_to_db()
    print(f'Added subject {name} with ID {subject.id}.\n')

def exit():
    """
    Prints exit message.
    """
    print('Bye bye!')

def list_subjects():
    """
    List all subjects.
    """
    # TODO: remove not a subject and actually list all subjcets properly
    subject = Subject('not a name')
    for id, name in subject.list_subjects():
        print(f'{id} {name} \n')

class MainMenu(Menu):
    """
    Main menu choices.
    """
    ADD_SUBJECT = ('Add subject', add_subject)
    LIST_SUBJECTS = ('List subjects', list_subjects)
    EXIT = ('Exit', exit)

def main_menu():
    """
    Shows main menu, until user exits.
    """
    print('Hi Tea!')
    while True:
        print('What can LogBook do for you today?')
        choice = input_choice(MainMenu)
        choice.functionality()
        if choice == MainMenu.EXIT:
            return


main_menu()