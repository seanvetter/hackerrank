
numtest = int(input())

s = []
for _ in range(numtest):
    s.append(input())

for userstring in s:
    # normal string
    # get length
    length = len(userstring)
    even = []
    odd = []
    for n in range(length):
        if n % 2 == 0: #even
            even.append(userstring[n])
        else: # odd
            odd.append(userstring[n])
    print("{0} {1}".format("".join(even), "".join(odd)))

