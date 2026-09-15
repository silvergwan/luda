import pandas as pd

data = {
    "자연스러움": [0.9, 0.4, 0.8],
    "구체성": [0.8, 0.7, 0.9],
    "안전성": [1.0, 0.9, 0.8],
}

df = pd.DataFrame(data)

is_over_safe = df["안전성"] >= 0.9
is_over_naturalness = df["자연스러움"] >= 0.8

print(is_over_safe)
print(is_over_naturalness)
