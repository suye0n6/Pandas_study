import pandas as pd

s = pd.DataFrame({'Bob' : ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.','Bland.']})

index=['2018', '2019', '2020', '2021']
YH = pd.Series([143, 150, 157, 160], index=index)
CS = pd.Series([165, 172, 180, 190], index=index)
growth = pd.DataFrame({
    '영희' : YH,
    '철수' : CS
})
growth

winemag = pd.read_csv("./winemag-data-130k-v2.csv")
winemag = pd.read_csv("./winemag-data-130k-v2.csv",index_col=0)
print(winemag)