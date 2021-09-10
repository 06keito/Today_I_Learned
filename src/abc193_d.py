import itertools

K = int(input())
S = str(input())
T = str(input())

cardpool = [K-(S.count(str(i))+T.count(str(i))) for i in range(1,10,1)]
total_card = sum(cardpool)
score_takahashi,score_aoki = 0,0
victory_precent = 0

for a in range(1,10,1):
    victory_cards,total = 0,0
    for b in range(1,10,1):
        S,T = S[:-1]+str(a),T[:-1]+str(b)
        score_takahashi = sum([i* 10**S.count(str(i)) for i in range(1,10,1)])
        score_aoki = sum([i* 10**T.count(str(i)) for i in range(1,10,1)])

        if score_takahashi>score_aoki:
            if a==b:
                victory_precent += (cardpool[a-1]/(total_card)) * ((cardpool[b-1]-1)/(total_card-1))
            else:
                victory_precent += (cardpool[a-1]/(total_card)) * (cardpool[b-1]/(total_card-1))

print(victory_precent)