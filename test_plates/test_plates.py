from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME ") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("123456") == False
    assert is_valid("A12345") == False
    assert is_valid("A1234567") == False