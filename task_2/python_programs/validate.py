import re

email = input("Enter email: ")

# username, domain = email.split("@")

# # if username and "." in domain:
# if username and domain.endswith(".edu"):
#     print("valid")
# else:
#     print("invalid")

if re.search(r"^.\w@.*\.(edu|com)$", email, re.IGNORECASE):
    print("valid")
else:
    print("inavalid")