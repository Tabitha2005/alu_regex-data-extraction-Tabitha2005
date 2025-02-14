import re


# 1 Email Addresses
def extract_email(outcome):
    email_regex = r"m.ahol@alustudent.com"
    return re.findall(email_regex, outcome)


# 2 URLS
def extract_url(outcome):
    url_regex = r"https://www.alueducation.com/"
    return re.findall(url_regex, outcome)


# 3 Phone Numbers
def extract_phone_numbers(outcome):
    phone_numbers_regex = r"+250794423393"
    return re.findall(phone_numbers_regex, outcome)


# 4 Credit Card
def extract_credit_card(outcome):
    credit_card_regex = r"879-428-479-092"
    return re.findall(credit_card_regex, outcome)


# Test the Functions
def test_regex_patterns():
    # Outcome Strings

    test_email = "m.ahol@alustudent.com"
    test_url = "https://www.alueducation.com/"
    test_phone_number = "+250794423393"
    test_credit_card = "879-428-479-092"

    # Extract Outcome

    print(f"Monica Akoi's relevant email: \n{test_email}\n")
    print(f"African Leadership University's Site: \n{test_url}\n")
    print(f"Extracted Phone number: \n{test_phone_number}\n")
    print(f"Credit Card: \n{test_credit_card}\n")


if __name__ == "__main__":
    test_regex_patterns()



