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

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
#print(s1)

df['F'] = s1

df.at[dates[0], 'A'] = 0

df.iat[0,1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

#print(df)

#측정되지 못하여 비어있는 데이터를 결측지라고 한다. pandas에서는 결측치를 np.nan으로 나타낸다.

#재인덱싱은 해당 축에 대하여 인덱스를 변경/추가/삭제를 하게된다. 이는 복사된 데이터프레임을 반환한다.

df1 = df.reindex(index=dates[0:4], columns=list(df.columns)+['E'])
df1.loc[dates[0]:dates[1], 'E' ] = 1

#결측치가 하나라도 존재하는 행들을 버리고 싶을 때는 dropna()매소드를 활용한다.
print(df1.dropna(how='any'))

#결측치가 있는 부분을 다른 값으로 채우고 싶다면 fillna() 매소드를 이용한다.
print(df1.fillna(value=5))

#결측치인지 아닌지의 여부 메소드
print(pd.isna(df1))