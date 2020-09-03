import models
import logging

try:

    if __name__ == '__main__':
        recruiter_one = models.Recruiter('mary', 'james', 'maryjames@mail.com', '932569357', '500', '5')
        programmer_one = models.Programmer('mick', 'colins', 'nickcolins@mail.com', '823659256', '600',
                                           ['Java', 'C#', 'C++'], '5')
        programmer_two = models.Programmer('leo', 'luck', 'leoluck@mail.com', '283569234', '450',
                                           ['Python', 'Java', 'PHP', 'Swift'], '10')
        candidate_one = models.Candidate('Edward Grey', 'edwardgrey@mail.com', ['Python', 'HTML', 'C#'], 'Python',
                                         'Upper Intermediate')
        candidate_two = models.Candidate('Simon Teon', 'simonteon@mail.com', ['Python', 'Java', 'SQL'], 'Java',
                                         'Upper Intermediate')
        candidate_three = models.Candidate('Christin May', 'christinmay@mail.com', ['JavaScript', 'PHP'], 'JavaScript',
                                           'Upper Intermediate')


except models.UnableToWorkException as e:
    logging.basicConfig(filename='logs.py', filemode='w', level=logging.INFO,
                        format='%(asctime)s')
    logging.exception(e)

except ValueError as a:
    logging.basicConfig(filename='logs.py', filemode='w', level=logging.INFO,
                        format="%(asctime)s")
    logging.exception(a)




