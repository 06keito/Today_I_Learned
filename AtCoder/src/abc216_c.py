def main():
    N = int(input())
    count = 120
    ans = ""

    for i in range(count):
        if N==0:
            break
        if N%2==1:
            N -= 1
            ans = "A" + ans
        elif N%2==0:
            N //= 2
            ans = "B" + ans
    print(ans)

if __name__ == "__main__":
    main()