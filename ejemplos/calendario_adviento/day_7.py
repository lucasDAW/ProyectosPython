import sys


with open('day_7.txt','r') as file:

    archivo = file.read()

lines = [line.split(": ") for line in archivo.splitlines()]
lines = [(int(test), list(map(int, args.split()))) for test, args in lines]

star, plus, concat = lambda x, y: x * y, lambda x, y: x + y, lambda x, y: int(f"{x}{y}")
def solve(targ, args, operators):
    def inner(targ, args, curr):
        if curr > targ:
            return False
        match args:
            case []:
                return curr == targ
            case [arg, *rest]:
                return any(inner(targ, rest, op(curr, arg)) for op in operators)

    return inner(targ, args[1:], args[0])


print(sum(targ for targ, args in lines if solve(targ, args, [star, plus])))
print(sum(targ for targ, args in lines if solve(targ, args, [star, plus, concat])))