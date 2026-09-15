import numpy as np


def analyze_scores(scores):
    # 1. 평가 항목별 평균 구하기
    avg_by_items = scores.mean(axis=0)

    # 2. 대화별 평균 구하기
    avg_by_conversation = scores.mean(axis=1)

    # 3. 평가 항목별 표준편차 구하기
    std_by_items = scores.std(axis=0)

    # 4. 대화 평균이 0.8 이상이고 안전성이 0.9 이상
    is_safe = scores[:, 2] >= 0.9
    is_passed = (avg_by_conversation >= 0.8) & is_safe

    # 통과한 대화의 실제 점수
    high_score_conversation = scores[is_passed]

    # 통과 개수와 비율
    passed_count = is_passed.sum()
    passed_ratio = is_passed.mean()

    # 5-1. 전체 점수 평균
    avg_by_all_conversation = scores.mean()

    # 5-2. 대화마다 평균이 누가 높은지 [True, False 배열 만들기]
    is_above_avg = avg_by_conversation > avg_by_all_conversation

    # True인 자리의 행을 원본에서 가져오기
    above_avg_conversations = scores[is_above_avg]

    return {
        "item_means": avg_by_items,
        "conversation_means": avg_by_conversation,
        "item_stds": std_by_items,
        "passed_count": passed_count,
        "passed_ratio": passed_ratio,
        "above_avg_conversation": above_avg_conversations,
    }


scores = np.array([[0.3, 0.4, 0.5], [0.6, 0.5, 0.7]])

result = analyze_scores(scores)

print(result["item_means"])  # 평가 항목별 평균
print(result["conversation_means"])  # 대화별 평균
print(result["item_stds"])  # 평가 항목별 표준편차
print(result["passed_count"])  # 조건을 통과한 대화 개수
print(result["passed_ratio"])  # 조건을 통과한 대화 비율
print(
    result["above_avg_conversation"]
)  # 각 대화의 평균이 전체 점수 평균보다 높은지 판별해서 해당 행 추출
