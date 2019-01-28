import hashlib


def generate(file):
    with open(file) as f:
        for line in f:
            h = hashlib.md5(line.encode('utf-8'))
            yield h.hexdigest()


for item in generate('C:\\Users\\Александр\\PycharmProjects\\Homework 2.2\\output.txt'):
    print(item)