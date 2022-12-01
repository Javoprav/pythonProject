def is_palindrome(word):
    word_ = ''
    for i in word:
        if i != "":
            word_ += i
    word_.islower()
    reversed_str = word_[::-1]
    if reversed_str == word_:
        return True
    else:
        return False

try:
    assert is_palindrome("level") == True
    assert is_palindrome("sagas") == True
    assert is_palindrome("hero") == False
    assert is_palindrome("drama") == False

except AssertionError:
    print("Неверно, проверьте функцию на разных значениях")

else:
    print("Все хорошо, все работает")