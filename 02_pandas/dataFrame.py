import pandas as pd

# Pandas의 데이터프레임은 행과 열에 이름이 붙은 표
data = {
    "자연스러움": [0.9, 0.4, 0.8],
    "구체성": [0.8, 0.7, 0.9],
    "안전성": [1.0, 0.9, 0.8],
}

# 딕셔너리의 키는 열이름, 리스트는 그 열에들어갈 값들이 된다, 왼쪽의 숫자는 행을 구분하는 인덱스
df = pd.DataFrame(data)

is_over_safe = df["안전성"] >= 0.9
is_over_naturalness = df["자연스러움"] >= 0.8

natural_conversations = df[is_over_naturalness]
over_score_conversation = df[is_over_safe & is_over_naturalness]

df["평균"] = df[["자연스러움", "구체성", "안전성"]].mean(axis=1)


print(is_over_safe)
print(is_over_naturalness)
print(natural_conversations)
print(over_score_conversation)


