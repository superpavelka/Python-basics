player = {}
player['name'] = input('Введите имя: ')
player['health'] = 100
player['damage'] = 50

enemy = {}
enemy['name'] = input('Введите имя: ')
enemy['health'] = 100
enemy['damage'] = 50

def attack(attacker, victim):
    victim['health'] -= attacker['damage']
    print(attacker['name'],' атакует ', victim['name'])
    print(attacker['name'],' наносит ', victim['name'], ' ', attacker['damage'], ' единиц урона')
    if victim['health'] < 1:
        print(f'{victim["name"]} мертв(а)')

attack(player, enemy)
attack(player, enemy)
