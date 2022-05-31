from collections import Counter


def is_contained(a, b):
    letters = Counter(b)
    letters.subtract(Counter(a))
    return all(v >= 0 for v in letters.values())


with open("words.txt", "r") as f:
    array = []
    for line in f:
        array.append(line.strip())
chars = input("Vnesi vse možne črke: ")

while True:
    length = int(input("Vnesi dolžino besede: "))
    if length == 0:
        chars = input("Vnesi vse možne črke: ")
        length = int(input("Vnesi dolžino besede: "))
    f = open("words.txt", "r")
    for word in array:
        if len(word) != length:
            continue
        if is_contained(word, chars):
            print(word)
    print()
