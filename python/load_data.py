import pandas as pd
import psycopg2

# DB connection
conn = psycopg2.connect(
    host="localhost",
    database="seo-analytics-pipeline",
    user="postgres",
    password="12345"
)

df = pd.read_csv("data/seo_data.csv")

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute(
        
    """
    INSERT INTO seo_metrics (date, page, keyword, clicks, impressions, ctr, avg_position)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (date, page, keyword) DO NOTHING
    """,
    (row['date'], row['page'], row['keyword'], row['clicks'], row['impressions'], row['ctr'], row['avg_position'])
)

conn.commit()
cursor.close()
conn.close()

print("Data successfully inserted!")