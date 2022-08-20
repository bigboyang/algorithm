arr = ["Enter uid1234 Muzi"
    , "Enter uid4567 Prodo"
    ,"Leave uid1234"
    ,"Enter uid1234 Prodo"
    ,"Change uid4567 Ryan"]


def solution(record):
    answer = []
    dict = {}

    # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    for r in record:
        sp = r.split()
        if len(sp) == 3:
            dict[sp[1]] = sp[2] # id 최신화

    for r in record:
        sp = r.split()
        if sp[0] == 'Enter':
            answer.append(f"{dict[sp[1]]}님이 들어왔습니다.")
        elif sp[0] == 'Leave':
            answer.append(f"{dict[sp[1]]}님이 나갔습니다.")

    return answer

print(solution(arr))