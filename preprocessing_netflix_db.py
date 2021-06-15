import pandas as pd


netflix_db = pd.read_csv("netflix_titles.csv")
netflix_db.info()
print(netflix_db.head())
#print(netflix_db.isnull())    #stampa in per ogni riga true o false a seconda che il volre sia nullo o meno
print(netflix_db.isnull().sum())
#data la colonna il metodo fillna() sostituisce il valore NULL con uno preimpostato dal programmatore
netflix_db["director"].fillna("No available", inplace=True)
netflix_db["cast"].fillna("No available", inplace=True)
netflix_db["country"].fillna("No available", inplace=True)
netflix_db["date_added"].fillna("No available", inplace=True)
netflix_db["rating"].fillna("No available", inplace=True)
print("\n")
print(netflix_db.isnull().sum())

compression_opts = dict(method='zip', archive_name='netflix_titles_normalized.csv')
netflix_db.to_csv('netflix_titles_normalized.zip', index=False, compression=compression_opts)