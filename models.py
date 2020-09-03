from datetime import datetime, date

class Employee:

    def __init__(self, name, surname, email, phone, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.salary = salary
        self.validate_email()
        with open('e.txt', 'a+') as file:
            file.write(self.email + '\n')


    def validate_email(self):
        with open('e.txt') as file:
            lines = file.read().split('\n')
            if self.email in lines:
                raise ValueError('User with such email already exists')

    def work(self):
        return 'I came to the office'

    def salary_check(self, salary, days):
        return salary * days

    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def check_salary(self, salary):
        quantity_of_days = date.today() - date(year=date.today().year, month=date.today().month, day=1)
        quantity_of_weeks = (quantity_of_days.days + 1) // 7
        quantity_of_days_offs = quantity_of_weeks * 2
        quantity_of_business_days = quantity_of_days.days - quantity_of_days_offs
        return quantity_of_business_days * salary


class Recruiter(Employee):

    def __init__(self, name, surname, email, phone, salary, hired_this_month):
        Employee.__init__(self, name, surname, email, phone, salary)
        self.hired_this_month = hired_this_month

    def work(self):
        return super().work() + 'and start hiring'

    def __str__(self):
        return 'Recruiter : ' + self.name.capitalize() + ' ' + self.surname.capitalize()


class Programmer(Employee):

    def __init__(self, name, surname, email, phone, salary, tech_stack, closed_this_month):
        Employee.__init__(self, name, surname, email, phone, salary)
        self.tech_stack = tech_stack
        self.closed_this_month = int(closed_this_month)

    def work(self):
        return super().work() + 'and start programing'

    def __str__(self):
        return 'Programmer : ' + self.name.capitalize() + ' ' + self.surname.capitalize()

    def __lt__(self, other):
        return self.tech_stack < other.tech_stack

    def __gt__(self, other):
        return self.tech_stack > other.tech_stack

    def __eq__(self, other):
        return self.tech_stack == other.self_stack

    def alfa_programmer(self, other):
        return set(self.tech_stack + other.tech_stack), self.closed_this_month + other.closed_this_month


class Candidate:

    def __init__(self, full_name, email, technologies, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.technologies = technologies
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    def work(self):
        raise UnableToWorkException("I'm not hired yet, lol")

class Vacancy:

    def __init__(self, title, main_skill, main_skill_level):
        self.title = title
        self.main_skill = main_skill
        self.main_skill_level = main_skill_level


class UnableToWorkException(Exception):
    pass