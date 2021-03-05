import pandas as pd
df = pd.DataFrame([['Anna', 23, 3],['Sam', 36, 12],
              ['Bill', 33, 10],
              ['Moica', 25, 7],
              ['Lisa', 27, 7],
              ['Peter', 32, None]])
df.columns = [1,2,3]
df.rename(columns={1 : 'perviy'}, inplace=True)
df[4] = ['Мужской','Женский','Женский','Женский','Женский','Женский']
df[5] = df[4].astype('Мужской' == 0)
print(df)