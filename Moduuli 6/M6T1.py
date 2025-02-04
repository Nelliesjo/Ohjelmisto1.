import random

def noppa():
    return (random.randint(1, 6))


def paakoodi():
    while True:
        luku = noppa()
        print(f"heitto: {luku}")
        if luku == 6:
            break

paakoodi()
