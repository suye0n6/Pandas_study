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


outliers_iqr = df[(df['value'] < lower_bound) | (df['value'] > upper_bound)]

print("IQR 이상치 탐지 결과:")
print(f"Q1: {Q1:.2f}, Q3 : {Q3:.2f}, IQR: {IQR:.2f}")
print(f"하한: {lower_bound:.2f}, 상한: {upper_bound:.2f}")
print(f"이상치 개수: {len(outliers_iqr)}")
print(f"이상치 값들: {outliers_iqr['value'].values}")

#박스플롯으로 시각화
plt.figure(figsize=(10,6))
plt.boxplot(df['value'])
plt.title('박스플롯을 통한 이상치 탐지')
plt.ylabel('값')
plt.show()