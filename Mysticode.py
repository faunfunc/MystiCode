import time
import sys

def get_user_digit():
    user_digit = input('Enter the number of digits: ')
    
    if user_digit == '':
        print('Please enter a digit!')
    else:
        print('You entered the following digits: ' + user_digit)
        return user_digit
    
def digit_combo(user_digit):
    digit_length = len(user_digit)
    combo_num = 10
    total_combinations = pow(combo_num, digit_length)
    print('Total combinations' ,total_combinations)

    return total_combinations

def print_combo_util(user_digit, current_combo, index, file_handle):
    if index == len(user_digit):
        file_handle.write(current_combo + '\n')
        file_handle.flush()
        time.sleep(0.000001)
        return
    
    digit = user_digit[index]
    for i in range(10):
        new_combo = current_combo + str(i)
        print_combo_util(user_digit, new_combo, index + 1, file_handle)

def print_combo(user_digit):
    with open('Combinations.txt', 'w') as file:
        print('printing all combinations')
        time.sleep(3)
        print_combo_util(user_digit, "", 0, file)
    

def start_program(user_digit):
    # digit_combo(user_digit)
    total_combinations = digit_combo(user_digit)

    while True:
        generate_statement = input('generate all combinations: y/n | ')
    
        if generate_statement.lower() == 'y' :
            print('hold tight...')
            time.sleep(2)
            print('generating')
            time.sleep(3)
            print_combo(user_digit)
            print('combinations saved to Combinations.txt')
            break
        elif generate_statement.lower() == 'n':
            print('okay bye')
            input('press any key to exit')
            break

        else:
            print('invalid choice. Please enter "y" or "n" ')
            

user_input = get_user_digit()

while not user_input.isdigit():
    print('Enter a valid digit')
    user_input = get_user_digit()


start_program(user_input)
