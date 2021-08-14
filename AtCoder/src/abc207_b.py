import math

def main():
    A,B,C,D = map(int,input().split())
    if (B/C)>=D:
        print(-1)
    else:
        print(math.ceil(A/((C*D)-B)))

if __name__ == "__main__":
    main()