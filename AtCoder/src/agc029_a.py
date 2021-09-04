def main():
    S = str(input())
    ans = 0
    Bcount = 0

    for i in range(len(S)):
        if S[i]=="B":
            Bcount += 1
        if S[i]=="W":
            ans += Bcount
    print(ans)

if __name__ == '__main__':
    main()
