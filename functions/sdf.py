# message: str = ''.join([string for string in open('../data/msg.txt').readlines()])
message: str = [string for string in open('../data/msg.txt').readlines()]
print(message)