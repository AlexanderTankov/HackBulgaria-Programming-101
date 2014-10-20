class Hero:

    def __init__(self, name, health, nickname):
        self.name = name
        self.__MAX_HEALTH = health
        self.health = health
        self.nickname = nickname

    def known_as(self):
        return "%s the %s" % (self.name, self.nickname)

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
