def  main():
    N = int(input())
    r_array,l_array = [0]*N,[0]*N
    ans = 0

    for i in range(N):
        t,l_array[i],r_array[i] = map(int,input().split())
        if t==1:
            continue
        elif t==2:
            r_array[i] -= 0.5
        elif t==3:
            l_array[i] += 0.5 
        elif t==4:
            r_array[i] -= 0.5 
            l_array[i] += 0.5 

    for i in range(N):
        for j in range(i+1,N):
            ans += (max(l_array[i],l_array[j]) <= min(r_array[i],r_array[j])) # bool

    print(ans)


if __name__ == "__main__":
    main()