from collections import deque

def solution(queue1, queue2):
    answer = 0
    total = (sum(queue1) + sum(queue2))

    if total % 2 != 0:
        return -1

    total //= 2

    q1, q2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)

    while answer <= 600000: # 두개의 큐 최대 길이만큼 탐색
        if q1_sum == q2_sum:
            return answer
        elif q1_sum < q2_sum:
            q2_front = q2.popleft()
            q2_sum -= q2_front
            q1_sum += q2_front
            q1.append(q2_front)
        else:
            q1_front = q1.popleft()
            q1_sum -= q1_front
            q2_sum += q1_front
            q2.append(q1_front)

        answer += 1

    return -1