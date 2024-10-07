from character import Hero, Opponent, heroes_list, opponents_list
from weapon import bow, love, weapons_list

#var_weapon1 = input("Hi John choose your weapon:")
print("Choose your Hero!")
for hero in heroes_list:
    print(heroes_list.index(hero), hero.name)
hero = heroes_list[int(input())]
print(f"Choose your weapon {hero.name}!")
for weapon in weapons_list:
    print(weapons_list.index(weapon),weapon.name)
hero.equip(weapons_list[int(input())])
opponent = Opponent(name = "Jean", health = 100)


while True:
    hero.attack(opponent)
    opponent.attack(hero)

    hero.health_bar.draw()
    opponent.health_bar.draw()
    
    input()

    if hero.health <= 0:
        print(f"{opponent.name} win the game!")
        break    
    elif opponent.health <= 0:
        print(f"{hero.name} win the game")
        break

    