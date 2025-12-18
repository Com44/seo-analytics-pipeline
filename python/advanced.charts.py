import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connect to database
engine = create_engine("postgresql://postgres:12345@localhost:5432/seo-analytics-pipeline")

# CTR Over Time --------------------------------------
ctr_df = pd.read_sql("""
    SELECT
        date,
        SUM(clicks)::float / SUM(impressions) AS ctr
    FROM seo_metrics
    GROUP BY date
    ORDER BY date
""", engine)
ctr_df['date'] = pd.to_datetime(ctr_df['date'])

plt.plot(ctr_df["date"], ctr_df["ctr"])
plt.title("CTR Over Time")
plt.xlabel("Date")
plt.ylabel("CTR")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/CTR_Trend.png")
plt.clf()

# Ranking Trend --------------------------------------
rank_df = pd.read_sql("""
    SELECT
        date,
        AVG(avg_position) AS avg_position
    FROM seo_metrics
    GROUP BY date
    ORDER BY date
""", engine)
rank_df['date'] = pd.to_datetime(rank_df['date'])

plt.plot(rank_df["date"], rank_df["avg_position"])
plt.title("Average Ranking Over Time")
plt.xlabel("Date")
plt.ylabel("Average Position")
plt.gca().invert_yaxis()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/Ranking_Trend.png")
plt.clf()


# Top Keywords ----------------------------------------
keyword_df = pd.read_sql("""
    SELECT
        keyword,
        SUM(clicks) AS clicks
    FROM seo_metrics
    GROUP BY keyword
    ORDER BY clicks DESC
    LIMIT 5
""", engine)

plt.bar(keyword_df["keyword"], keyword_df["clicks"])
plt.title("Top Keywords by Clicks")
plt.xlabel("Keyword")
plt.ylabel("Total Clicks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/Top_Keywords.png")
plt.clf()

print("Charts created successfully!")