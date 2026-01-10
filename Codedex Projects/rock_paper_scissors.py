import random

print('===================\nRock Paper Scissors\n===================')
print('1) ✊\n2) ✋\n3) ✌️')

player = int(input(('Enter your choice: ')))
computer = random.randint(1,3)

choices = ['✊','✋','✌️']
# print(f'You chose: {choices[player-1]}')
# print(f'CPU chose: {choices[computer-1]}')

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
elif player == 3:
    print("You chose: ✌️")
else:
    print("Invalid choice")

if computer == 1:
    print("CPU chose: ✊")
elif computer == 2:
    print("CPU chose: ✋")
else:
    print("CPU chose: ✌️")

if player == computer:
    print('Tie')

elif(player == 1 and computer == 3) or\
    (player == 2 and computer == 1) or\
    (player == 3 and computer == 2):
    print('You won')

else:
    print('CPU won')