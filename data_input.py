import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Series 기본
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#Dataframe 기본
dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

#Dataframe 여러 칼럼
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
print(df.tail(3))

#첫 5개 행의 데이터를 보여준다
df.head()

#마지막 3개 행의 데이터를 보여준다
df.tail()

#DataFrame 인덱스 ()괄호 사용 금지
df.index
print(df.index)

#DataFrame 칼럼
df.columns

#DataFrame 값
df.values

#DataFrame의 평균 통계값
print(df.describe())

#열과 행을 바꾼 형태의 데이터프레임
df.T

#메소드로 행과 열 나타내기
#axis 는 인덱스 기준 / ascending 은 오름차순(기본값)
print(df.sort_index(axis=1, ascending=False))

print(df.sort_values(by='B'))

#데이터 선택하기

#A라이는 이름을 가진 칼럼의 데이터만 가져온다.
df['A']

print(df['A'])

type(df['A'])

print(type(df['A']))

#특정 행 범위 슬라이싱으로 가져오기
df[0:3]

#인덱스명에 해당하는 값들 가져오기
df['20130102' : '20130104']

#특정 행만 가져오고 싶을 때는 주의
df['20130102' : '20130102']

#이름을 이용하여 선택하기
print(df.loc[dates[0]])

#칼럼에 대한 모든 값 가져오기
print(df.loc[:,['A','B']])

#인덱스에 따른 모든 값 가져오기
print(df.loc['20130102' : '20130104' , ['A','B']])

#특정 인덱스 값의 컬럼 값 가져오기
print(df.loc[dates[0], ['A', 'B']])

#.at도 가능하다
df.at[dates[0], 'A']

