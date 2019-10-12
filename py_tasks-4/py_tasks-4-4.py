player = {}
player['name'] = input('Введите имя: ')
player['health'] = 100
player['damage'] = 50
player['armor'] = 1.2

enemy = {}
enemy['name'] = input('Введите имя: ')
enemy['health'] = 100
enemy['damage'] = 50
enemy['armor'] = 1.2

def attack(attacker, victim):
    victim['health'] -= calc_damage(attacker['damage'], victim['armor'])
    print(attacker['name'],' атакует ', victim['name'])
    print(attacker['name'],' наносит ', victim['name'], ' ', calc_damage(attacker['damage'], victim['armor']), ' единиц урона')
    if victim['health'] < 1:
        print(f'{victim["name"]} мертв(а)')
def calc_damage(damage, armor):
    return round(damage/armor, 2)

attack(player, enemy)
attack(player, enemy)
attack(player, enemy)