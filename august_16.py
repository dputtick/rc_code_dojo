# naive looping solution

n = int(input())
for _ in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    acc = a
    for i in range(a+1, b+1):
        acc = a & i
    print(acc)


# optimized bit manipulation solution

def make_list(n):
    unpadded_num = [int(i) for i in list(bin(n)[2:])]
    padding = [0]*(32-len(unpadded_num))
    return padding + unpadded_num


def solve(args):
    a, b = make_list(args[0]), make_list(args[1])
    c = [0]*32
    for i in range(32):
        if a[i] == b[i]:
            c[i] = a[i]
        else:
            break
    strings = [str(n) for n in c]
    return int(''.join(strings), 2)
    

n = int(input())
for _ in range(n):
    a, b = input().split()
    ab_tuple = (int(a), int(b))
    print(solve(ab_tuple))