import numpy as np
# 1. 배열의 모양 출력
# 2. 평가 항목별 평균과 표준편차
# 3. 대화별 평균
# 4. 평균이 0.8 이상이고 안전성이 0.9 이상인 대화 추출
# 5. 위 조건을 통과한 대화의 개수와 비율
# 6. 각 대화의 평균이 전체 점수 평균보다 높은지 판별해서 해당 행 추출


# 열: 자연스러움, 구체성, 안전성
scores = np.array(
    [
        [0.9, 0.8, 1.0],
        [0.4, 0.7, 0.9],
        [0.8, 0.9, 0.8],
        [0.3, 0.2, 0.9],
        [0.9, 0.9, 0.9],
        [0.7, 0.6, 1.0],
    ]
)

# 2. 평가 항목별 평균과 표준 편차
avg_by_items = scores.mean(axis=0)
std_by_items = scores.std(axis=0)

# 1. 배열의 모양 출력
print(scores.shape)

# 3. 대화별 평균, 4. 조건 1 평균이 0.8 이상
avg_by_conversation = scores.mean(axis=1)

# 4. 조건 2 안정성이 0.9 이상
is_safe = scores[:, 2] >= 0.9

is_high_quality = is_safe & (avg_by_conversation >= 0.8)

high_score_conversations = scores[is_high_quality]

# 5. 위 조건을 통과한 대화의 개수와 비율
passed_count = is_high_quality.sum()
passed_ratio = is_high_quality.mean()

# 6. 각 대화의 평균이 전체 점수 평균보다 높은지 판별해서 해당 행 추출

# 6-1. 전체 점수 평균
avg_by_all_conversation = scores.mean()

# 대화마다 전체 평균보다 높은지 확인 → True/False 배열
is_above_avg = avg_by_conversation > avg_by_all_conversation

# True인 자리의 행을 원본에서 가져오기
above_avg_conversations = scores[is_above_avg]

print(above_avg_conversations)
