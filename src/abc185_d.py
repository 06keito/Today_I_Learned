import math

def corner(N,M):
    if M==0:
        print(1)
        exit()
    elif N==M:
        print(0)
        exit()

def add_value_to_list(N,array):
    array.sort(reverse=True)
    if array[-1]!=1:
        array.append(0)
    if array[0]!=N:
        array.insert(0,N+1)
    return array

def main():
    N,M = map(int,input().split())
    corner(N,M)
    array = list(map(int,input().split()))
    array = add_value_to_list(N,array)
    ans,interval = 0,[]
    
    for i in range(len(array)-1):
        if array[i]-array[i+1]!=1:
            interval.append(array[i]-array[i+1]-1)

    step = min(interval)

    for i in interval:
        ans += math.ceil(i/step)
    #print(array)
    #print(interval)
    print(ans)

if __name__ == "__main__":
    main()