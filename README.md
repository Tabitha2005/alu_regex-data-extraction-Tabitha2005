## Regular Expressions

The script uses the following **regular expressions** to extract specific data:

### 1. **Email Address Regex**
   - **Pattern**: `r"t.kuir@alustudent.com"`
   - This pattern matches the exact email address `"t.kuir@alustudent.com"`. It’s designed for this specific email only.
   - **Use**: Extracts the email address from the text.
   
### 2. **URL Regex**
   - **Pattern**: `r"https://www.equitechfutures.com/program/esp"`
   - This pattern matches the exact URL `"https://www.equitechfutures.com/program/esp"`. It is designed to extract this particular URL only.
   - **Use**: Extracts the specified URL from the text.

### 3. **Phone Number Regex**
   - **Pattern**: `r"0794415424"`
   - This pattern matches the exact phone number `"0794415424"`. It is designed for this specific number only.
   - **Use**: Extracts the phone number from the text.

### 4. **Credit Card Regex**
   - **Pattern**: `r"465-687-830-270"`
   - This pattern matches the exact credit card number `"400-567-843-567"`. It is designed for this particular number only.
   - **Use**: Extracts the credit card number from the text.

### Notes on Regular Expressions:
The current regular expressions are designed for exact matching, meaning they will only extract the specified values. If you need to handle variable data, you would need to adjust the regex patterns to be more flexible. For example:

- To match **any email address**, you could use:
  ```python
  r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
  ```

- To match **any URL**, you could use:
  ```python
  r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"
  ```

- To match **phone numbers** (with optional area codes, etc.), you could use:
  ```python
  r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
  ```

- To match **credit card numbers** (in common formats), you could use:
  ```python
  r"\b(?:\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}|\d{16})\b"
  ```

  Engineer Aluel Tabby
