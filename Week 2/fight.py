import random


class Fight():

    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def who_is_first(self):
        if random.randint(0, 100) < 50:
            return self.hero
        return self.orc

    def simulate_fight(self):
        attacker = self.who_is_first()
        if attacker == self.hero:
            attacked = self.orc
        else:
            attacked = self.hero

        while self.hero.is_alive() and self.orc.is_alive():
            damage = attacker.attack()
            attacked.take_damage(damage)

            attacked, attacker = attacker, attacked
