from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    reporters = defaultdict(set)
    cnt = defaultdict(int)

    for kakao in report:
        reporter, criminal = kakao.split(" ")
        reporters[reporter].add(criminal)
        cnt[criminal] += 1

    for kakao in id_list:
        resultCnt = 0
        for rp in reporters[kakao]:
            if cnt[rp] >= k:
                resultCnt += 1
        answer.append(resultCnt)

    return answer