import pandas as pd
import numpy as np

data = {
    'name' : ['김철수', '이영희', '박민수', '최지영', '정현우'],
    'age' : [25, 30, np.nan, 28, 35],
    'salary' : [3000, np.nan, 4500, 3800, np.nan],
    'department' : ['It', 'HR', 'IT', np.nan, 'IT']
}

df = pd.DataFrame(data)
print(df)

#결측값 확인
print("\n결측값 개수 : ")
print(df.isnull().sum())

print("\n결측값 비율:")
print(df.isnull().sum() / len(df) * 100)

#결측값 삭제
df_drop_rows = df.dropna()
print("행 삭제 후 데이터:")
print(df_drop_rows)

#열 단위 삭제
df_drop_cols = df.dropna(axis=1, thresh=3)
print("\n열 삭제 후 데이터:")
print(df_drop_cols)

#결측값 대체
df['age_filled'] = df['age'].fillna(df['age'].mean())
print("나이 평균값 대체:")
print(df[['name', 'age', 'age_filled']])

#중앙값으로 대체
df['salary_filled'] = df['salary'].fillna(df['salary'].median())
print("\n급여 중앙값으로 대체:")
print(df[['name', 'salary','salary_filled']])

#최빈값으로 대체(범주형 변수)
df['department_filled'] = df['department'].fillna(df['department'].mode()[0])
print("\n부서 최빈값 대체:")
print(df[['name', 'department', 'department_filled']])

#선형 보간
df['age_interpolated'] = df['age'].interpolate(method='linear')
print("나이 선형 보간:")
print(df[['name', 'age', 'age_interpolated']])