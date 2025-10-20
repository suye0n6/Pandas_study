import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Series 기본
s = pd.Series([1, 3, 5, np.nan, 6, 8])
#print(s)

#Dataframe 기본
dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#print(df)

#Dataframe 여러 칼럼
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})
#print(df.tail(3))

#위치 기준으로 선택하기 (인덱스 3을 뜻함)
print(df.iloc[3])

#위치 기준으로 선택하기 (행, 열)
print(df.iloc[3:5, 0:2])

#행과 열의 인덱스를 리스트로 넘겨줄 수도 있다. 
print(df.iloc[[1,2,4], [0,2]])

#명시적으로 행이나 열 선택 인자에 : 슬라이스를 전달하면 다음과 같이 행 또는 열 전체를 가져올 수 있다.
print(df.iloc[1:3,:])

#값 하나를 선택하기 위해서는 특정 행, 열 지정하는 방식으로
df.iloc[1,1]

#조건을 이용하여 선택하기 (A열에 있는 수가 양수인 값만 추출)
print(df[df.A > 0])

#각 값을 기준으로 조건 만들기 (음수는 다 NaN으로 표기)
print(df[df > 0])

#값 필터링
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

#print(df2)

print(df2[df2['E'].isin(['two','four'])])