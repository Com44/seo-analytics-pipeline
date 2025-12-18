-- ===============================
-- SEO ANALYTICS – INSIGHTS SQL
-- ===============================

-- 1️⃣ Total Clicks
SELECT SUM(clicks) AS total_clicks FROM seo_metrics;

-- 2️⃣ Total Impressions
SELECT SUM(impressions) AS total_impressions FROM seo_metrics;

-- 3️⃣ Average CTR
SELECT AVG(ctr) AS avg_ctr FROM seo_metrics;

-- 4️⃣ Average Ranking Position
SELECT AVG(avg_position) AS avg_position FROM seo_metrics;

-- 5️⃣ Clicks over time
SELECT date, SUM(clicks)
FROM seo_metrics
GROUP BY date ORDER BY date;

-- 6️⃣ Top keywords by clicks
SELECT keyword, SUM(clicks) AS total_clicks
FROM seo_metrics
GROUP BY keyword
ORDER BY total_clicks DESC
LIMIT 10;

-- 7️⃣ Top pages by impressions
SELECT page, SUM(impressions) AS total_impressions
FROM seo_metrics
GROUP BY page
ORDER BY total_impressions DESC
LIMIT 10;

-- 8️⃣ Best CTR keywords
SELECT keyword, AVG(ctr) AS avg_ctr
FROM seo_metrics
WHERE impressions > 100
GROUP BY keyword
ORDER BY avg_ctr DESC
LIMIT 10;

-- 9️⃣ Keyword ranking improvements over time
SELECT date, keyword, AVG(avg_position) AS avg_position
FROM seo_metrics
GROUP BY date, keyword
ORDER BY date, avg_position;

-- 🔟 Performance under CTR threshold
SELECT *
FROM seo_metrics
WHERE ctr < 0.03;

SELECT * FROM seo_metrics LIMIT 10;