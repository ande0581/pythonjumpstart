import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):  # This is the representation of the class, helps when printing value or debugging
        return "Creature: {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        print('The Wizard {} attacks {}!'.format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print('You roll {} ...'.format(my_roll))
        print('{} rolls {} ...'.format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print('The Wizard has handily defeated {}'.format(creature.name))
            return True
        else:
            print('The Wizard has been DEFEATED')
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()  # this takes the value from the base Creature Class
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)  # this takes the value from the base Creature Class
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()  # this takes the value from the base Creature Class
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier





