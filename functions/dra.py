
f = open('../data/msg.txt')
msg: str = ''.join(x for x in f.readlines())
print(msg)