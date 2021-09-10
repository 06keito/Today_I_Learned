def main():
    H,W,N = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(N)]

    array = sorted(array,key=lambda x: x[0])
    for i in range(N):
        array[i][0] = i+1

    array = sorted(array,key=lambda x: x[1])

    for i in range(N):
        array[i][1] = i+1

    for i in range(N):
        print(array[i][0],array[i][1])

if __name__ == '__main__':
    main()