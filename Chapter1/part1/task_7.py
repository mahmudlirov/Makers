def biggest_guy(one, two, three) -> object:
    return max(one, two, three)
    ListofNumbers = (one, two, three)
    MaxNumber = max(ListofNumbers)
    return(MaxNumber)
biggest_guy(3, 9, 30)

def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("WRONG!!")
        return
print("SUCCESS!!!")
#test your code by un-commenting the line(s) below
test_biggest_guy()