def is_odd(number):
    (number > 0)
        return True
    (number == 0)
        return False
    """if number % 2 == 1:
        return True
    else:
        return False"""

def test_is_odd():
    assert is_odd(2) == False
    assert is_odd(3) == True
    assert is_odd(8) == False
    assert is_odd(100) == False
    assert is_odd(101) == True
    print("YOUR CODE IS CORRECT!")
#test your code by un-commenting the line(s) below
test_is_odd()