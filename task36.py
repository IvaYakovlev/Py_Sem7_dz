inp = input().split()
res = tuple(map(lambda x: tuple(x.split('=')),inp))
print(res)