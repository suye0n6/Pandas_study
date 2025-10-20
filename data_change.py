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
#print(df.tail(3))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)

df['F'] = s1

df.at[dates[0], 'A'] = 0

df.iat[0,1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

print(df)