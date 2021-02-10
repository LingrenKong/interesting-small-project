from datetime import date
d1 = date.today() #2020-4-4
d2 = date(2020,4,1)
delta = d2- d1 # datetime.timedelta(days=-3)
d2<d1 #True
print(d1+delta) # d2 2020-04-01

import pandas as pd
df = pd.Series()
df.loc[0] = 1
df = df.reindex(index=list(df.index)+['add'])
df.loc['add'] = 2
