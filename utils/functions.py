'Utility functions for the game PyLife2'
# PyLife2 utility functions
# Written by ry00001 (hello@ry00001.me)
# This is free and open-source software.

import random, sys, os # pylint: disable=C0410

def gender():
    'Returns a random gender.'
    return random.choice(['male', 'female'])

def name(arg_g=False):
    'Returns a random name.'
    if arg_g: # woman
        return random.choice(open('content/names_g.txt').read().split('\n')) # pylint: disable=R1710
    else: # man
        return random.choice(open('content/names.txt').read().split('\n')) # pylint: disable=R1710

def surname():
    'Returns a random surname.'
    return random.choice(open('content/surnames.txt').read().split('\n')) # pylint: disable=R1710

def wait_key(prompt):
    ''' Wait for a key press on the console and return it. '''
    print(prompt)
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result
