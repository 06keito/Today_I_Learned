#https://atcoder.jp/contests/abc057/tasks/abc057_c

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    #divisors.sort()
    return divisors

N = int(input())
list =  make_divisors(N)
ans = 10**9
if len(list)%2==1:
    list.append(list[-1])
for i in range(0,len(list),2):
    tmp1 = len(str(list[i]))
    tmp2 = len(str(list[i+1]))
    ans = min(ans,max(tmp1,tmp2))
print(ans)

