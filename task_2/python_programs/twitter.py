import re

url = input("URL is: ").strip()
#http|https//www.twitter.com//user_name

# username=url.replace("https//www.twitter.com//", "")
# print(username)

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(username)

username = re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url)
if username:
    print(username.group(1))


