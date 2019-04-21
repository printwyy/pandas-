import pandas as pd

df=pd.read_csv('test_set.csv',)

c=df['marital']

c2=c.copy()

for i in range(len(c)):
    if(c2[i]=='single'):
        c2[i]='1'
    if (c2[i] == 'divorced'):
        c2[i] = '2'
    if(c2[i]=='married'):
        c2[i]='3'

df['marital']=c2

print(c2)
df.drop(df.columns[0], axis=1, inplace=True)
print(df)
df.to_csv('test_set.csv')