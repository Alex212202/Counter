import random

random_choice = random.randint(0, 2)

if random_choice == 0:
    computer_choice = 'камень'
elif random_choice == 1:
    computer_choice = 'бумагу'
else:
    computer_choice = 'ножницы'

user_choice = input('камень,ножницы или бумага?\n')
print('Вы выбрали', user_choice + ', комп\'ютер выбрал', computer_choice)

if computer_choice == user_choice:
    winner = 'Ничья'
elif computer_choice == 'бумага' and user_choice == 'камень':
    winner = 'Комп\'ютер'
elif computer_choice == 'камень' and user_choice == 'ножницы':
    winner = 'Комп\'ютер'
elif computer_choice == 'ножницы' and user_choice == 'бумага':
    winner = 'Комп\'ютер'
else:
    winner = 'Пользователь'

print(winner, 'выиграл!')
