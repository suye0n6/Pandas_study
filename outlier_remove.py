import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# 샘플 데이터 생성
np.random.seed(42)
data = np.random.normal(100, 15, 1000)
# 이상치 추가
data = np.append(data, [200, 250, 50, 30])

df = pd.DataFrame({'value': data})


#IRQ 계산
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

#이상치 경계 설정
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#이상치 제거 
df_clean = df[(df['value']>= lower_bound) & (df['value'] <= upper_bound)]
print(f"원본 데이터 크기: {len(df)}")
print(f"이상치 제거 후 데이터 크기: {len(df_clean)}")

#이상치 대체
df_capped = df.copy()
df_capped['value_capped'] = df_capped['value'].clip(lower=lower_bound, upper=upper_bound)

print("이상치 대체 결과: ")
print(df_capped[['value', 'value_capped']].head(10))

#이상치 변환
df_log = df.copy()
df_log['value_log'] = np.log(df_log['value'])

plt.figure(figsize=(12,4))

plt.subplot(1,2,1)
plt.hist(df_log['value'], bins=30, alpha=0.7)
plt.title('원본 데이터')

plt.subplot(1, 2, 2)
plt.hist(df_log['value_log'], bins=30, alpha=0.7)
plt.title('로그 변환 후 데이터')

plt.tight_layout()
plt.show()