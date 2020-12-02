class Password:
    def __init__(self, minApp, maxApp, char, password):
        self.minApp = int(minApp)
        self.maxApp = int(maxApp)
        self.char = char
        self.password = password

    def get_char_appearance(self):
        return self.password.count(self.char)

    def check_if_valid(self):
        return self.minApp <= self.get_char_appearance() <= self.maxApp

    def official_check_if_valid(self):
        return (self.password[self.minApp-1] == self.char) ^ (self.password[self.maxApp-1] == self.char)


passwords = []

with open("passwords.txt", "r") as file:
    for line in file:
        params = line.split(" ")
        min_max = params[0].split("-")
        params[1] = params[1][:-1]
        passwords.append(Password(*min_max, params[1], params[2]))


def count_valid_passwords():
    count = 0
    for password in passwords:
        if password.official_check_if_valid():
            count = count+1
    print(count)


count_valid_passwords()

