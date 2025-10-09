# ⚽ English premier League (2021-2023) Data analysis,Visualizations & Interactive Power-BI Dashboard

## 📉📈Project Overview
This project focuses on analyzing Data from the English premier league from **2021 to 2023** using **Python (pandas)**, **Postgres** and **Power-Bi**
The goal was to clean, transform, analyze using python(pandas)showing some minor visualizations with **matplotlib** for easy understanding of some events during that period the premier league,then creating and loading the dataset into **Postgres** database for some important queries and important columns addition  for easy understanding,finally laoded the dataset into **power-BI** to build an interactive dashboard to enhance understanding of key-insights.

----

## 🧰Tools & Technologies Used
-- **Python:** Data cleaning,Analzying and little Visualization(Pandas,Matplotlib)
-- **Postgres:** Querying data for deeper analysis and addition of vital columns
-- **Power-BI:** Dashboard creation for Data visualizations of key analysis
-- **PARQUET/CSV:** Data source format

## 📚 Process Summary
1. **Data Cleaning (Python):**
    Removed missing values, Dropped duplicates and the Link column because it was not needed
    Renamed columns in caps for easy call out and better view
    Converted the date column from object to date-time
    Converted the year column from float to integer cause i needed it for analysis
    Saved both Csv and parquet file type cause parquet easily saves changes in a data-set more than a Csv file

2. **Exploratory Data Analysis:**
    Explored: 
    - Total goals scored across three years
    - Total goals scored per year across the three years by Home teams and Away teams
    - Match results to check home wins,away wins and draws
    - Total fouls committed     
    - Total yellow cards given
    - Total red cards gievn
    - Average attendance per stadium

3. **Postgres:**
    created a database for the project to run some important queries like:
    - Top scoring stadiums
    - Top 5 teams with the most draws
    - Top 10 teams with the most wins
    - most matches played at each stadium

4. **Power BI Dashboard**    
    Designed an interactive dashboard showing:
    - Sum of attendance across the three whole seasons
    - Top 10 teams with most goals 
    - The number of goals scored per year by Home and Away teams
    - Total fouls committed across the whole 3 seasons by home and away teams
    - Top 5 teams with most draws
    - Top 10 home team wins across 3 years
    - Number of cards shown across 3 years(red card and yellow cards)

---

## Key Insights
- Manchester city(Ethihad) recorded the most Home wins(21) across the three years followed by liverpool(Anfield)20 because of the dominant style of play of both teams and fans 
- 2020 recorded more goals(748) than any other year.
- Away teams committed more fouls than the home teams because of the lack of comfortability usually caused by the home fans, and home teams are more comfortable at home so the make less mistakes and less fouls.
- Most goals was scored at Leeds united stadium (Elland Road), cause of the lesser quality in the team against other top premier league teams, so they conceded easily even at Home.
- manchester united (old trafford) recorded the most attendance over 3 years (2161502)

---
## 📷 Dashboard Preview
![Power BI Dashboard](visualizations/dashboard_preview.png)

##  ✍Author
**Paul Eru**
_Data Analyst | Python | Power BI| SQL_

📩 **Email:** paul.eru@yahoo.com
🔗[Github](https://github.com/Thisizeru)