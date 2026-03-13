import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

year = 2021
month = 1

tripdata_prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
tripdata_csv = f'{tripdata_prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

#tripdata = pd.read_parquet('./yellow_tripdata.parquet')

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


def run():
    pg_username = 'root'
    pg_password = 'root'
    pg_db = 'ny_taxi'
    pg_port = '5433'
    pg_host = 'localhost'

    tripdata = pd.read_csv(tripdata_csv,dtype=dtype,parse_dates=parse_dates,iterator=True,chunksize=100000)
    engine = create_engine(f'postgresql://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

    first = True

    for chunk in tqdm(tripdata):
        if first:
            chunk.head(0).to_sql(name='yellow_taxi_trip_data',con=engine,if_exists='replace')
            first = False
        chunk.to_sql(name='yellow_taxi_trip_data',con=engine,if_exists='append')

if __name__ == '__main__':
    run()


