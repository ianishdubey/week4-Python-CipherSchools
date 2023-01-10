# else and finally clause in exception handling


while True:
    try:
        number = int(input('enter a number : '))
    except ValueError:
        print("You didn\'t entered integer")
    except:
        print('unexpected error !! s')
    else:
        print(f'user input = {number}')
        break
    finally:
        print('finally blocks .......... ')
