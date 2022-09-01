from logging import critical
import random

#def tiradaMaestria(cant, dif):
#    success = 0
#    for i in range(0, cant):
#        roll = random.randint(1,10)
#        if roll >= dif:
#            print(f' {roll}!')
#            success += 1
#        else:
#            print(f' {roll}')
#    return success

def tiradas(cant, dif, mas):
    success = 0
    critical = 0
    for i in range(0, cant):
        roll = random.randint(1,10)
        if roll == 1:
            print(f' {roll}!')
            success -= 1
        elif (roll == 10):
            print(f' {roll}! Critical Success!')
            success += 1
            critical += 1
        elif roll >= dif:
            print(f' {roll}!')
            success += 1
        else:
            print(f' {roll}')
    if mas:
        success += tiradas(critical, dif, mas)
    return success

def main():
    dice_rolls = int(input('Cuantos dados? '))
    dificulty = int(input('Dificultad? '))
    mastery = int(input('Maestria? 1 = SI / 0 = NO: '))
    successes = 0
    successes = tiradas(dice_rolls, dificulty, mastery)
    if successes < 0:
        print(f'0 exitos')
    else:
        print(f'{successes} exitos')

if __name__== "__main__":
    main()