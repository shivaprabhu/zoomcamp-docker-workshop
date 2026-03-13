import sys
import pandas as pd

month = sys.argv[1]

df = pd.DataFrame({"day_of_month":[1,2],"no_of_rides":[3,4]})
df["month"] = month

df.to_parquet(f"parquet_ride_data_{month}")

print(df.head()) 