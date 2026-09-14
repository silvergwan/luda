# Numpy 종합 문제
import numpy as np
# 평가 항목별 평균
# 대화별 평균
# 대화 평균이 0.8 이상이면서, 안전성이 0.9 이상인 행 전체

scores = np.array([[0.9, 0.8, 1.0], [0.4, 0.7, 0.9], [0.8, 0.9, 0.8], [0.3, 0.2, 0.9]])
# 열: 자연스러움, 구체성, 안전성

# 평가 항목별 평균
avg_score_by_item = scores.mean(axis=0)

# 대화별 평균
avg_score_by_conversation = scores.mean(axis=1)

low_naturalness = scores[:, 0] < 0.7

result = scores[(low_naturalness) | (avg_score_by_conversation < 0.8)]

print(result)
