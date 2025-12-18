DROP TABLE IF EXISTS seo_metrics;

CREATE TABLE seo_metrics (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    page TEXT NOT NULL,          -- new column
    keyword TEXT NOT NULL,       -- new column
    clicks INT,
    impressions INT,
    ctr DECIMAL(5,3),
    avg_position DECIMAL(5,2),
    UNIQUE(date, page, keyword)
);