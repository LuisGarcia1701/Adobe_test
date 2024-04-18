import test_3

#Positive assert test using a valid email format
def test_valid_email():
    assert test_3.valid_email_format("adobe@codechallenge.com") == True

#Negative assert test unsing an invalid email format
def test_invalid_email():
    assert test_3.valid_email_format("1adobe@codechallenge.com") == False

#replicate test for each case of valid or invalid format