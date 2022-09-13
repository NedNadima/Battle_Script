from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#Create black magic
fire= Spell("Fire", 25, 100, "black")
thunder= Spell("Thunder", 25, 100, "black")
blizzard= Spell("Blizzard", 40, 100, "black")
quake= Spell("Quake", 15, 100, "black")

#Create white magic
cure = Spell("Cure", 55, 120, "white")
viagra = Spell("Viagra", 30, 120, "white")

#Create some Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP of one party member", 9999999)
grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#Player magic
player_spells = [fire, thunder, blizzard, quake, cure, viagra]
player_items = [{"item":potion,"quantity":5}, {"item":hipotion,"quantity":10},
                {"item":superpotion, "quantity":20}, {"item":elixer, "quantity":2},
                {"item":hielixer, "quantity":9},{"item":grenade, "quantity":1}]

player1 = Person("Jon :",4360, 165, 400, 34, player_spells, player_items)
player2 = Person("Ned :",4650, 195, 400, 34, player_spells, player_items)
player3 = Person("Rafa:",4560, 105, 130, 34, player_spells, player_items)

enemy1 = Person("Magi:", 12200, 995, 545, 25, player_spells, player_items)
enemy2 = Person("Mogu:", 12200, 34, 845, 25, player_spells, player_items)
enemy3 = Person("Boni:", 12200, 94, 945, 232, player_spells, player_items)

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("================")

    print("\n")
    print("Name                   HP                                      MP")

    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("Choose action:")
        index = int(choice)-1

        if index == 0:
            dmg = player.generate_damage()
            enemy= player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You attacked "+ enemies[enemy].name + "for", dmg, "points of damage. Enemy HP:")

            if enemies[enemy].get_hp()==0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) -1
            if magic_choice == -1:
                continue

            spell= player.magic[magic_choice]
            magic_dmg = spell.generate_damage()
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL+ "\nNot enough MP\n" + bcolors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE+ "\n" + spell.name + "heals for", str(magic_dmg), "HP"+ bcolors.ENDC)

            elif spell.type == "black":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose item: " ))-1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            if player.items[item_choice]["quantity"] == 0:
                 print("None left")
                 continue
            player.items[item_choice]["quantity"]-= 1



            if item.type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name +" heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixer":
                if item.name == "elixer":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                print(bcolors.OKGREEN + "\n" + item.name + "Fully restores HP/MP"+ bcolors.ENDC)
            elif item.type == "attack":

                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name +" deals", str(item.prop), "points of damage" + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

    enemy_choice = 1
    target = random.randrange(0,3)
    enemy_dmg = enemies[0].generate_damage()

    players[target].take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP:", player.get_hp())


    print("Your HP:",bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp())+ bcolors.ENDC + "\n")
    print("Your MP:",bcolors.OKBLUE + str(player.get_mp())+ "/" + str(player.get_max_mp())+ bcolors.ENDC + "\n")

    defeated_enemies = 0
    defeated_players = 0

    for enemy in enemies:
        if enemy.get_hp()==0:
            defeated_enemies += 1

    for player in players:
        if player.get_hp ==0:
            defeated_players += 1


    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False

    elif defeated_players == 2:
        print(bcolors.FAIL + "Your enemies have defeated you!" + bcolors.ENDC)
        running = False