import pandas as pd

path = ''
netflix_db = pd.read_csv(path)
netflix_db.info()
print(netflix_db.head())
# print(netflix_db.isnull())    #stampa per ogni riga true o false a seconda del valore nullo o meno
print(netflix_db.isnull().sum())
# data la colonna il metodo fillna() sostituisce il valore NULL con uno pre-impostato dal programmatore
netflix_db["director"].fillna("No available", inplace=True)
netflix_db["cast"].fillna("No available", inplace=True)
netflix_db["country"].fillna("No available", inplace=True)
netflix_db["date_added"].fillna("No available", inplace=True)
netflix_db["rating"].fillna("No available", inplace=True)
print("\n")
print(netflix_db.isnull().sum())

compression_opts = dict(method='zip', archive_name='netflix_titles_normalized.csv')
netflix_db.to_csv('netflix_titles_normalized.zip', index=False, compression=compression_opts)