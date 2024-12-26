import webbrowser

baseURL = "https://www.instagram.com/"

usernames = open("notFollowers.txt", "r")

check = 0

while True:
    for i in range(10):
        username = usernames.readline().strip()
        if username is None or "":
            check = 1
            break

        tempURL = baseURL + username

        if i == 0: webbrowser.open_new(tempURL)
        else: webbrowser.open_new_tab(tempURL)
    
    input("press enter for next 10 usernames")

    if check == 1:
        break


