N,M = map(int,input().split())
lst = [list(map(int,input().split())) for i in range(M)]
p = list(map(int,input().split()))
ans = 0

for bit in range(2**N):
    power = ['off']*N
    switch_even_odd_check = [0]*M
    flag = True

    for i in range(N):
        if (bit>>i)&1:
            power[i] = 'on'

    for j,turn_on_list in enumerate(lst):        
        for idx in turn_on_list[1:]:
            if power[idx-1]=='on':
                switch_even_odd_check[j] += 1
    
    for eo,light in zip(switch_even_odd_check,p):
        if eo%2!=light:
            flag = False
            break

    if flag==True:
        ans += 1

print(ans)