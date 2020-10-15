# Taken from mission The Vampires

# Taken from mission The Defenders

# Taken from mission Army Battles

# Taken from mission The Warriors

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:  # пока оба живы
        unit_2.health, unit_1.health = unit_2 - unit_1  # обычный, вампиризм
        # проверяем выжил ли
        if unit_2.is_alive:
            unit_1.health, unit_2.health = unit_1 - unit_2  # обычный, вампиризм
    if unit_1.is_alive:
        return True
    return False


# урон наполовину
def fight_half(unit_1, unit_2):  # атакующий, защищающийся
    unit_2.health = unit_1 / unit_2


class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False

    # проверка наличия аттрибутов (если нету, значение = 0)
    def is_attribute(self, object_battle):
        health = object_battle.health
        attack = object_battle.attack
        if hasattr(object_battle, "defence"):
            defence = object_battle.defence
        else:
            defence = 0
        if hasattr(object_battle, "vampirism"):
            vampirism = object_battle.vampirism
        else:
            vampirism = 0
        return health, attack, defence, vampirism  # возвращаем кортеж

    # сравнение 'защиты' и 'атаки'
    def compare(self, defence, attack):
        if defence > attack:
            return True
        return False  # если 'атака' больше 'защиты'

    def __sub__(self, other):
        a1 = self.is_attribute(self)  # получаем кортеж с атрибутами
        a2 = self.is_attribute(other)  # получаем кортеж с атрибутами
        # бой
        if self.compare(a2[2], a1[1]):  # если защита больше атаки
            res1 = a2[0]  # урон не проходит
            res2 = a1[0]
        else:
            res1 = a1[0] - (a2[1] - a1[2])  # атака-защита: для self.health
            # вампиризм
            res2 = a2[0] + (((a2[1] - a1[2]) * a2[3]) // 100)  # для other.health
        return res1, res2  # возвращаем новые значения .health


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defence = 2


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.attack = 6

    def __truediv__(self, other):  # атакующий, защищающийся
        a1 = self.is_attribute(self)  # атакующий
        a2 = self.is_attribute(other)  # защищающийся
        a = int(a1[1] * .5)  # полатаки
        # расчет половины удара
        if self.compare(a2[2], a):  # если защита больше атаки
            res = a2[0]  # урон не проходит
        else:
            res = a2[0] - (a - a2[2])
        return res


class Army():
    def __init__(self):
        self.command = []

    def add_units(self, units, count):
        for i in range(count):
            self.command.append(units())
    #
    # @property
    # def is_alive(self):
    #     if self.army:
    #         return True
    #     return False


class Battle():
    def fight(self, army_01, army_02):
        while army_01.command and army_02.command:
            if fight(army_01.command[0], army_02.command[0]):

                # для битвы с Lancer
                if len(army_02.command) >= 2 and isinstance(army_01.command[0], Lancer) :  # если есть второй боец в армии, то ему полурона
                    fight_half(army_01.command[0], army_02.command[1])
                    if army_02.command[1].is_alive is False:
                        army_02.command.pop(1)

                army_02.command.pop(0)
            else:
                army_01.command.pop(0)
        if army_01.command:
            return True
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
