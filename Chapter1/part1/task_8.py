def choice_to_number(choice):
    """Convert choice to number."""
    choice = input("choice your name: 'Usain', 'Me', 'Aybek' ")
    choice = {1:'Usain', 2:'Me', 3:'Aybek',}
    if choice == 'Usain':
        return choice['Usain']
    elif choice == 'Me':
        return choice['Me']
    elif choice == 'Aybek':
        return choice['Aybek']
    else:
        print('code is not correct')

# If choice is Usain you should get back 1.
def number_to_choice(number):
    if number == 1:
        return number_to_choice['Usain']
    elif number == 2:
        return number_to_choice['Me']
    elif number == 3:
        return number_to_choice['Aybek']
    else:
        return('code is not correct')
# if number is 1 then return usain bolt.dc
#DO NOT remove lines below here, this is designed to test your code.
def test_choice_to_number():
    assert choice_to_number('Usain') == 1
    assert choice_to_number('Me') == 2
    assert choice_to_number('Aybek') == 3
def test_number_to_choice():
    assert number_to_choice(1) == 'Usain'
    assert number_to_choice(2) == 'Me'
    assert number_to_choice(3) == 'Aybek'
def test_all():
    try:
        test_choice_to_number()
        test_number_to_choice()
    except AssertionError:
        print('WRONG')
    else:
        print('SUCCESS')
#test your code by un-commenting the line(s) below
test_all()