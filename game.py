'PyLife2 itself.'

# PYLIFE2
# Alpha Version

# Written by ry00001 (hello@ry00001.me, ry00001#3487)

from classes import human # pylint: disable=E0611
# heck off pylint, it works good

import json # pylint: disable=C0411
from utils import functions

META = json.load(open('content/meta.json'))

print(open('content/title.txt').read().replace('{ver}', META['version']))

class Game:
    'The PyLife2 game itself.'
    def __init__(self, o_pop=20):
        self.people = []
        self.orig_population = o_pop
        self.year = 0
        self.populate()
        # placeholder for now, memes incoming

    def log(self, msg, _type='Game'):
        'Log a message'
        print(f'[{_type}] {msg}')

    def populate(self):
        'Populate the game'
        self.people = [human.Human(self) for i in range(self.orig_population)]
        if META['debug']:
            [self.log(i.fullname + ' generated.', 'Generation') for i in self.people] # pylint: disable=W0106

GAME = Game()
PROMPT = 'Press any key to continue...'

print(f'Press ESC to exit the game at the "{PROMPT}" prompts.')

while True:
    GAME.year += 1
    GAME.log(f'It is now year {GAME.year}')
    for i in GAME.people:
        if not i.dead:
            i.tick()
        i.atick()
    if functions.wait_key(PROMPT) == b'\x1b':
        print('ESC was pressed. Exiting...')
        exit(0)
