
"""Script to extract all unique tract_id from ``mxm_dataset.db``"""

import sqlite3

import pandas as pd



if __name__ == '__main__':
    all_track_ids = pd.read_csv('track_ids.csv')
    cnx = sqlite3.connect(r'.\data\mxm_dataset.db')
    all_track_ids = set()
    sql_gen = pd.read_sql_query(r"SELECT * FROM lyrics", cnx, chunksize=500)
    for i, chunk in enumerate(sql_gen):
        all_track_ids.update(chunk['track_id'].unique())
        if i % 100 == 0:
            print(i)
    cnx.close()
    print("Saving...")
    data = {'track_id': list(all_track_ids)}
    df = pd.DataFrame(data)
    df.to_csv(r'.\data\track_ids.csv', index=False)
