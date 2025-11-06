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

# Z-Score 계산
z_scores = np.abs(stats.zscore(df['value']))
outliers_zscore = df[z_scores > 3]

print("Z-Score 이상치 탐지 결과:")
print(f"이상치 개수: {len(outliers_zscore)}")
print(f"이상치 값들: {outliers_zscore['value'].values}")

# 시각화
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.hist(df['value'], bins=30, alpha=0.7)
plt.axvline(df['value'].mean(), color='red', linestyle='--', label='Mean')
plt.title('데이터 분포')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(range(len(df)), df['value'], alpha=0.6)
plt.scatter(outliers_zscore.index, outliers_zscore['value'], 
           color='red', s=100, label='Outliers')
plt.title('Z-Score 이상치 탐지')
plt.legend()

plt.tight_layout()
plt.show()


