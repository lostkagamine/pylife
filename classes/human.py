'Human class for the game PyLife2'
# PyLife2 Human class
# Written by ry00001 (hello@ry00001.me)
# This is free and open-source software.

from utils import functions

import random # pylint: disable=C0411

class Human:
    'Just a human.'
    def __init__(self, game, name=None, surname=None, gender=None):
        self.game = game
        if gender is None:
            self.gender = functions.gender()
            self.bgender = True if self.gender == 'female' else False
        self.name = functions.name(self.bgender) if name is None else name
        self.surname = functions.surname() if surname is None else surname
        self.dead = False
        self.age = 0
        self.fullname = f'{self.name} {self.surname}'
        self.job = None
        self.money = 200

    def tick(self): # runs every year except when dead
        'This runs every year until dead.'
        self.age += 1 # age up
        if random.randrange(1, 100) == 50:
            self.die('of an unfortunate event')

    def atick(self):
        'This runs every year. Even when dead.'
        pass

    def die(self, cause):
        'Kills said person.'
        self.game.log(f'{self.fullname} has died {cause}. They were {self.age} when they died.', 'Deaths') # pylint: disable=C0301
        self.dead = True
