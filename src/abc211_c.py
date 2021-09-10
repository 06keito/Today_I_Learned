def dp(n,name,dict):
    return 0

def main():
    S = str(input())
    name = ['c','h','o','k','u','d','a','i']
    mod = 10**9+7
    dict = {}

    for n,i in enumerate(S):
        if i in name:
            dict.setdefault(i,[]).append(n)
    print(dict)
    counter(7,name,dict)


if __name__ == "__main__":
    main()