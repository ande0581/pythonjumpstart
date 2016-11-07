import random
import time

from app7_wizard.actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------------')
    print('     Wizard Battle')
    print('-------------------------')
    print('')


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, scaliness=75, breaths_fire=True),
        Wizard('Evil Wizard', 1000),
    ]

    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'.format(
            active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?  ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)  # If the creatures been been defeated, remove from game
            else:
                print('The Wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The Wizard returns revitalized')
        elif cmd == 'r':
            print('The Wizard has become unsure of his power and he flees!!')
        elif cmd == 'l':
            print('The Wizard {} takes in the surroundings and sees:')
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print('OK, exiting game...bye!')
            break

        if not creatures:
            print('You defeated all the creatures, well done!')
            break

if __name__ == '__main__':
    main()