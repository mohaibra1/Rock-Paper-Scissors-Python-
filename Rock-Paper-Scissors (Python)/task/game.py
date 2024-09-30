# Write your code here
import random

choose = ['scissors', 'rock', 'paper', '!rating']
players = {}
comp_choose = ['water','dragon','devil', 'gun', 'rock','fire', 'scissors',  'snake',
               'human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'lightning', '!rating']
rotated_list_1 = []

def computer():
    rand = random.randint(0, 2)
    return choose[rand]

def rotate_list(r_list, index):
    global rotated_list_1
    r_list.pop(index)
    middle = int((len(r_list))/2)
    start_list = r_list[index+1:]

    for i in range(index, len(r_list)):
        if len(rotated_list_1) != middle:
            rotated_list_1.append(r_list[int(i)])
            #r_list.pop(int(i))
    for j in r_list:
        if len(rotated_list_1) != middle:
            rotated_list_1.append(j)
def complex_rules(innput, user_input, name):
    global rotated_list_1
    split_input = innput.split(',')
    index = split_input.index(user_input)
    comp_num = random.randint(0, len(split_input)-1)
    comp_ch = split_input[comp_num]
    rotate_list(split_input, index)
    if user_input == comp_ch:
        players[name] += 50
        print(f'There is a draw {user_input}')
    elif comp_ch in rotated_list_1:
        print(f'Sorry, but the computer chose {comp_ch}')
    else:
        players[name] += 100
        print(f'Well done. The computer chose {comp_ch} and failed')
    rotated_list_1.clear()
def rules(player, comp, name):
    if player == 'scissors' and comp == 'rock':
        print(f'Sorry, but the computer chose {comp}')
    elif player == 'rock' and comp == 'scissors':
        players[name] += 100
        print(f'Well done. The computer chose {comp} and failed')
    elif player == 'scissors' and comp == 'paper':
        players[name] += 100
        print(f'Well done. The computer chose {comp} and failed')
    elif player == 'paper' and comp == 'scissors':
        print(f'Sorry, but the computer chose {comp}')
    elif player == 'rock' and comp == 'paper':
        print(f'Sorry, but the computer chose {comp}')
    elif player == 'paper' and comp == 'rock':
        players[name] += 100
        print(f'Well done. The computer chose {comp} and failed')
    else:
        players[name] += 50
        print(f'There is a draw {player}')


def invalid_input(innput):
    if innput not in comp_choose:
        return True
    return False


def initialize_player(name):
    global players

    f_name = open('rating.txt', 'r')
    for line in f_name:
        line = line.strip()
        line = line.split()
        if line[0] == name:
            players[name] = int(line[1])
            break
        else:
            players[name] = 0
            break
    f_name.close()

def play():
    bye = True
    print('Enter your name:')
    name = input()
    print(f'Hello, {name}')
    initialize_player(name)
    inn = input()
    print("Okay, let's start")
    while bye:
        user_input = input()
        if user_input == '!exit':
            bye = False
            print('Bye!')
            break
        if invalid_input(user_input) and inn == '':
            print('Invalid input')
            continue
        if user_input == '!rating':
            print(f'Your rating: {players[name]}')
            continue
        if inn == '':
            comp = computer()  # computer plays
            rules(user_input, comp, name)
        else:
            complex_rules(inn, user_input, name)


play()