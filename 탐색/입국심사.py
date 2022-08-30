

def solution(n, times):
    answer = 0

    left, right = min(times), max(times)*n # 심사에 걸리는 최대시간과 최소시간

    while left <= right:
        people = 0 # 심사한 사람 수
        mid = (left+right)//2 # 이 시간(mid) 안에 몇명 심사 가능한지

        for t in times:
            people += mid//t

        # 모든 심사관들의 심사가 끝나고
        if people < n: # 더 많은 시간이 필요한 경우
            left = mid+1
        else: # people >= n, 시간이 충분한 경우 -> 시간을 줄여도 됨
            answer = mid  # 혹, 지금이 심사가능한 최적의 시간일지도 모르니
            right = mid - 1

    return answer



print(solution(6,[7, 10]))