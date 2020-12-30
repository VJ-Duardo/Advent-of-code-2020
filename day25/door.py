card_key, door_key = 0, 0
with open("keys.txt") as file:
    card_key, door_key = [int(k) for k in file.read().splitlines()]


SUBJECT_NUMBER = 7
DIVISER = 20201227

def get_loop_size(public_key):
    c = 0
    num = 1
    while num != public_key:
        num *= SUBJECT_NUMBER
        num = num % DIVISER
        c += 1
    return c


def get_encryption_key():
    card_loop_size = get_loop_size(card_key)

    encr_key = 1
    for i in range(card_loop_size):
        encr_key *= door_key
        encr_key = encr_key % DIVISER

    return encr_key


print(get_encryption_key())
