import itertools

def main():
    S,K = input().split()
    tmp = list(set(itertools.permutations(list(S),len(S))))
    array = [list(i) for i in tmp]
    array.sort()
    print("".join(array[int(K)-1]))


if __name__ == '__main__':
    main()