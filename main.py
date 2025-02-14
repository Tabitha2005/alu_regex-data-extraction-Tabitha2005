import re


# 1 Email Addresses
def extract_email(test):
    email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(email_regex, test)


# 2 URLS
def extract_url(test):
    url_regex = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
    return re.findall(url_regex, test)


# 3 Phone Numbers
def extract_phone_numbers(test):
    phone_numbers_regex = r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    return re.findall(phone_numbers_regex, test)


# 4 Credit Card
def extract_credit_card(test):
    credit_card_regex = r"\b(?:\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}|\d{16})\b"
    return re.findall(credit_card_regex, test)


# Test the Functions
def test_regex_patterns():

    # Test Strings Outcome

    test_email = "t.kuir@alustudent.com"
    test_url = "https://www.equitechfutures.com/"
    test_phone_number = "0794415424"
    test_credit_card = "453-354-123-456"

    # Extract Data

    print(f"Aluel extract email: \n{test_email}\n")
    print(f"Equitech Futures Site: \n{test_url}\n")
    print(f"Aluel Tabby's phone number: \n{test_phone_number}\n")
    print(f"My personal credit card: \n{test_credit_card}\n")


if __name__ == "__main__":
    test_regex_patterns()



