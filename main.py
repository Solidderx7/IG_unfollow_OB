from bs4 import BeautifulSoup

# load html files
with open('following.html', 'r', encoding='utf-8') as file:
    following = file.read()
with open('followers.html', 'r', encoding='utf-8') as file:
    followers = file.read()

# parsing html files
soup_following = BeautifulSoup(following, 'html.parser')
soup_followers = BeautifulSoup(followers, 'html.parser')

# get following
spans_following = soup_following.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
ids_following = [span.text.strip() for span in spans_following]

# get followers
spans_followers = soup_followers.find_all('span', class_="_ap3a _aaco _aacw _aacx _aad7 _aade")
ids_followers = [span.text.strip() for span in spans_followers]

# open file to write not followers
notFollowers = open("notFollowers.txt", "w")

total = 0

# find following that are not followers 
for id_following in ids_following:
    if id_following not in ids_followers:
        total += 1
        notFollowers.write(id_following + "\n")

notFollowers.close()

print("There are {} people that don't follow you back".format(total))
