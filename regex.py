import re

text = "Contact us at: john@email.com or call 123-456-7890"

# Find email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Emails found:", emails)

# Find phone numbers
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print("Phones found:", phones)

# Replace sensitive info
cleaned = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 
                '[EMAIL]', text)
print("Cleaned:", cleaned)
    