import sys
import pandas as pd

df = pd.DataFrame({'day':[1,2],'passengers':[15,24]})
month = int(sys.argv[1])

print(f'pipeline_month={month}')
df['month'] = [1,2]
print(df.head())
df.to_parquet(f'output_{month}.parquet')