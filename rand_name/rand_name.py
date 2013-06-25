from random import random, randint

letter_histogram = (('a', 8.167),
('b', 1.492),
('c', 2.782),
('d', 4.253),
('e', 12.70),
('f', 2.228),
('g', 2.015),
('h', 6.094),
('i', 6.966),
('j', 0.153),
('k', 0.772),
('l', 4.025),
('m', 2.406),
('n', 6.749),
('o', 7.507),
('p', 1.929),
('q', 0.095),
('r', 5.987),
('s', 6.327),
('t', 9.056),
('u', 2.758),
('v', 0.978),
('w', 2.360),
('x', 0.150),
('y', 1.974),
('z', 0.074))

def generate_letter():
    dist_sum = random() * 100

    for letter_stat in letter_histogram:
        dist_sum -= letter_stat[1]
        if dist_sum < 0:
            return letter_stat[0]

def generate_name():
    name_length = randint(4, 15)

    name = ""
    for i in range(name_length):
        name += generate_letter()

    return name


print generate_name()