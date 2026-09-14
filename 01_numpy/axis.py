# 복습 문제 (불린인덱싱, axis)
# 행 평균이 5 이상인 행 전체를 골라내는 코드
import numpy as np

arr = np.array([[2, 8], [6, 4], [1, 3]])

avg_arr = arr.mean(axis=1)

over_arr = arr[avg_arr >= 5]

print(over_arr)
