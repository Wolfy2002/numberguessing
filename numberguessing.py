import random

guessesTaken = 0

number = random.randint(1, 10)
print('Ma gandesc la un numar intre 1 si 10.\nAi voie 6 incercari.')

global guess

for guessesTaken in range(6):
    print('Ghiceste:')
    guess = int(input())

    if guess < number:
        guessesTaken += 1
        print('Ai ghicit un numar mai mic.')
    elif guess > number:
        guessesTaken += 1
        print('Ai ghicit un numar mai mare.')
    elif guess == number:
        print(f'Felicitari! Ai ghicit numarul in {guessesTaken} incercari.')
        break

if guess != number:
    print(f'Ai gresit! Numarul la care ma gandeam a fost {number} si ai avut {guessesTaken} incercari gresite.')

