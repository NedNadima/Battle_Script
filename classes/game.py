import random
from .magic import Spell
from .inventory import Item



class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self,name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp -= dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i= 1
        print("ACTIONS")
        for item in self.action:
            print("    "+ str(i) + ":",item)
            i += 1

    def choose_magic(self):
        print("MAGIC")
        i=1
        for spell in self.magic:
            print("    "+ str(i)+ ":",spell.name)
            i += 1

    def choose_item(self):
        print("ITEMS")
        i=1
        print(bcolors.OKGREEN + bcolors.BOLD + "ITEMS: " + bcolors.ENDC)
        for item in self.items:
            print("    "+ str(i)+ ". ", item["item"].name, ":", item["item"].description)
            i += 1

    def get_stats(self):
        print("                   _________________        ___________")
        print(bcolors.BOLD + str(self.name)+"     " +
              str(self.hp)+"/" + str(self.maxhp) + "   |" + bcolors.OKGREEN + " ██████████     |   " + bcolors.ENDC + bcolors.BOLD + "|   " +
              str(self.mp)+"/"+ str(self.maxmp) + "|" + bcolors.OKBLUE + "████████|" + bcolors.ENDC + "|")


