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

print(df.apply(np.cumsum))

#람다 함수
print(df.apply(lambda x: x.max() - x.min()))

# 히스토그램 구하기
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)


print(s.value_counts())

#문자열 메소드
s = pd.Series(['A','B','C','Aaba','Baca', np.nan, 'CABA', 'dog', 'cat'])

print(s.str.lower())

#concat
df = pd.DataFrame(np.random.randn(10, 4))

pieces = [df[:3], df[3:7], df[7:]]

print(pd.concat(pieces))

left = pd.DataFrame({'key' : ['foo','foo'], 'lavl' : [1,2]})
print(left)

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})

merged = pd.merge(left, right, on='key')

print(merged)

#append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])

s = df.iloc[3]

df.append(s, ignore_index=True)
