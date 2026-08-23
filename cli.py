from enum import Enum

from tabulate import tabulate

from model.dataClass.assessmentDataClass import AssessmentDataClass
from model.dataClass.subjectDataClass import SubjectDataClass

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
    subject = SubjectDataClass(name=name)
    subject_id: int = subject.create_subject(name=name)
    print(f'Added subject {name} with ID {subject_id}.\n')

def exit_cli():
    """
    Prints exit message.
    """
    print('Bye bye!')

def list_subjects():
    """
    List all subjects.
    """
    subjects = SubjectDataClass.get_all_subjects()
    for subject in subjects:
        print(f'ID: {subject.get('id')}, Name: {subject.get('name')}')

def list_assessments_for_subject():
    """
    List all assessments for subject with name.
    """
    subject = input('Name of subject: ')

    assessments = AssessmentDataClass.get_assessments_for_subject(subject)

    print(f"Here is a list of assessments for {subject}")
    for a in assessments:
        print(f'ID: {a.get('id')}, Title: {a.get('title')}, Due date: {a.get('dueDate')}')

def get_aggregate_of_assessments_by_type():
    """
    List count of assessments by type for subject.
    """
    data = AssessmentDataClass.get_assessment_count_for_subject_by_type()

    headers = {
        "subject_name": "Subject",
        "final_exam": "Final",
        "oral_exam": "Oral",
        "midterm_exam": "Midterm",
        "course_paper": "Paper",
        "homework": "Homework",
        "project": "Project",
        "quiz": "Quiz",
        "total": "Total"
    }

    print(tabulate(data, headers=headers, tablefmt="rounded_outline"))

class MainMenu(Menu):
    """
    Main menu choices.
    """
    ADD_SUBJECT = ('Add subject', add_subject)
    LIST_SUBJECTS = ('List subjects', list_subjects)
    LIST_ASSESSMENTS_FOR_SUBJECT = ('List assessments for subject', list_assessments_for_subject)
    ASSESSMENTS_TABLE = ('Assessments table', get_aggregate_of_assessments_by_type)
    EXIT = ('Exit', exit_cli)

def main_menu():
    """
    Shows main menu, until user exits.
    """
    print('Hi Tea!')
    while True:
        print('\n')
        print('What can LogBook do for you today?')
        choice = input_choice(MainMenu)
        choice.functionality()
        if choice == MainMenu.EXIT:
            return


main_menu()