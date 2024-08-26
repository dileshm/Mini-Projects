import re

email_pattern = re.compile(r"(^[a-aA-Z0-9_.+-@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
test_email = "VisualCode@outlook.com"

password_pattern = re.compile(r"[A-Za-z0-9$%@]{8,}\.")
test_password = "SuperSecret2024."

a = pattern.search(test_email)
check = password_pattern.fullmatch(test_password)
print(check)
