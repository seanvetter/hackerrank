
entries = int(input())

book = {}
for _ in range(entries):
    friend, number = input().strip().split(" ")
    book[friend] = number

#print(book)
while True:
    ask = input()
    if ask in book:
        print("{0}={1}".format(ask, book[ask]))
    else:
        print('Not found')
