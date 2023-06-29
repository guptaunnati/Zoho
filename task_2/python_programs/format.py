import re

name = input("Enter name: ").strip()
# matches = re.search("^(.+), *(.+)$", name)
# if matches:
#     last, first= matches.groups()
#     name= f"{first} {last}"

if matches := re.search("^(.+), *(.+)$", name):
    name = matches.group(2)+" "+matches.group(1)
print(name)