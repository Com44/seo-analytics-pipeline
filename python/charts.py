import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

conn = psycopg2.connect(
    host="localhost",
    database="seo-analytics-pipeline",
    user="postgres",
    password="12345"
)

df = pd.read_sql("SELECT date, SUM(clicks) AS clicks FROM seo_metrics GROUP BY date ORDER BY date", conn)
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(10,6))
plt.plot(df['date'], df['clicks'], marker='o')
plt.title("Total Clicks Over Time")
plt.xlabel("Date")
plt.ylabel("Clicks")
plt.grid()
plt.savefig("charts/clicks_over_time.png")
plt.show()