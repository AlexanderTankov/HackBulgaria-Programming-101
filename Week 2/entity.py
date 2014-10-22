from weapon import Weapon


class Entity():
    def __init__(self, name, health):
        self.name = name
        self.__MAX_HEALTH = health
        self.health = health
        self.damage = 0
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

    def take_healing(self, healing_points):
        if self.health == 0:
            return False
        if self.__MAX_HEALTH < self.health + healing_points:
            self.health = self.__MAX_HEALTH
        else:
            self.health += healing_points
        return True

    def has_weapon(self):
        return self.weapon

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.damage = weapon.damage

    def attack(self):
        return self.damage
