import copy

def main():
    N,K = map(int,input().split())
    array = list(map(int,input().split()))
    per_person_value = K//N
    surplus_value = K%N

    preferred_person_id = copy.copy(array)
    preferred_person_id.sort()
    preferred_person_id = set(preferred_person_id[:surplus_value])

    for i in array:
        if i in preferred_person_id:
            print(per_person_value+1)
        else:
            print(per_person_value)
            
if __name__ == "__main__":
    main()