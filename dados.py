import random

def main():
    dice_rolls = int(input('Cuantos dados? '))
    dificulty = int(input('Dificultad? '))
    #mastery = bool(input('Tiene maestria?'))
    successes = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1,10)
        if roll == 1:
            print(f' {roll}!')
            successes -= 1
        elif (roll == 10):
            print(f' {roll}! Critical Success!')
            successes += 1
        elif roll >= dificulty:
            print(f' {roll}!')
            successes += 1
        else:
            print(f' {roll}')
    if successes < 0:
        print(f'0 exitos')
    else:
        print(f'{successes} exitos')

if __name__== "__main__":
    main()