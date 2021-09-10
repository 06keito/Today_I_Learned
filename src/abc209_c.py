class Value():
    N = int(input())
    array = list(map(int,input().split()))
    mod = 10**9+7

    def __init__(self) -> None:
        pass

def main():
    ans = 1
    Value.array.sort()
    for i in range(Value.N):
        ans = ans*max(0,Value.array[i]-i) % Value.mod
    print(ans)

if __name__ == "__main__":
    main()