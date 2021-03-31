while True:
    try: 
        game_end = input("Welcome to 7-Up; Enter your number: ")
        float(game_end)
        break
    except:
        print('Error')

order_choice = input('Enter Yes to start first or No for CPU start: ')

#Variables
prop_num = int(game_end) + 1
keyword = '7-Up'
end = 0

while order_choice not in ['Yes','No']:
    print('Error')
    order_choice = input('Enter Yes to start first or No for CPU start: ')

#Player Start
if order_choice == 'Yes':
    print('*GAME START*')
    for num in range(1, prop_num):
        if num % 2 != 0:
            value = input(' Enter number or 7-UP: ')
            try:
                if num % 7 == 0 or '7' in str(num):
                    if value != '7-Up':
                        print('You Lose!')
                        end = 1
                        break
                elif int(value) != num:
                    print('You Lose!')
                    end = 1
                    break
            except:
                print('You Lose!')
                end = 1
                break
        else:
            if num % 7 == 0 or '7' in str(num):
                print(keyword)
            else:
                print(num)

#CPU Start
if order_choice != 'Yes':
    print('*GAME START*' )
    for num in range(1, prop_num):
        if num % 2 == 0:
            value = input('Enter number or 7-UP: ')
            try:
                if num % 7 == 0 or '7' in str(num):
                    if value != '7-Up':
                        print('You Lose!')
                        end = 1
                        break
                elif int(value) != num:
                    print('You Lose!')
                    end = 1
                    break
            except:
                print('You Lose!')
                end = 1
                break
        else:
            if num % 7 == 0 or '7' in str(num):
                print(keyword)
            else:
                print(num)
#Win Status
if end != 1:
    print('You Win!')
