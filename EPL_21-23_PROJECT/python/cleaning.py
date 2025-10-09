import pandas as pd

df= pd.read_csv("Epl\Epl2023.csv")
print(df)

#CLEANING THE DATASET
#1.CHECKING FOR DULPICATES
df.duplicated().sum()

#got 5 duplicated rows,but does bot affect the dataset but might as well remove them
df = df.drop_duplicates()

#droping the link column,cause i dont need it for my analysis
df.drop(labels="links",
        axis="columns",
        inplace= True)

#checking missing values
print(df.isnull().sum())

#isnull values was already replaced with 0


# renaming columns just for easy call outs
changes_in_column_names={"date":"DATE",
                          "clock":"TIME",
                          "statdium":"STADIUM",
                           "class":"CLASS",
                           "stadium":"STADIUM",
                           "attendance":"ATTENDANCE",
                            "Home Team" : "HOME TEAM",
                            "Goals Home": "HOME TEAM GOALS",
                            "Away Goals":"AWAY TEAM GOALS",
                            "Away Team": "AWAY TEAM",
                            "home_possessions":"HOME POSSESSIONS",
                            "away_possessions":"AWAY POSSESSIONS",
                            "home_shots": "HOME SHOTS",
                            "away_shots": "AWAY SHOTS",
                            "home_on": "HOME ON(SUBS)",
                            "away_on": "AWAY ON(SUBS)",
                            "home_off": "HOME OFF(SUBS)",
                            "away_off": "AWAY OFF(SUBS)",
                            "home_blocked":"HOME BLOCKED SHOTS",
                            "away_blocked": "AWAY BLOCKED SHOTS",
                            "home_pass": "HOME PASSES",
                            "away_pass": "AWAY PASSES",
                            "home_chances":"HOME CHANCES",
                            "away_chances": "AWAY CHANCES",
                            "home_corners":"HOME CORNERS",
                            "away_corners":"AWAY CORNERS",
                            "home_offside": "HOME OFFSIDES",
                            "away_offside": "AWAY OFFSIDES",
                            "home_tackles":"HOME TACKLES",
                            "away_tackles": "AWAY TACKLES",
                            "home_duels": "HOME DUELS WON",
                            "away_duels": "AWAY DUELS WON",
                            "home_saves": "HOME SAVES",
                            "away_saves": "AWAY SAVES",
                            "home_fouls": "HOME FOULS",
                            "away_fouls": "AWAY FOULS",
                            "home_yellow": "HOME YELLOW CARDS",
                            "away_yellow": "AWAY YELLOW CARDS",
                            "home_red" :"HOME RED CARDS",
                            "away_red": "AWAY RED CARDS",
                            "match_results":"MATCH RESULTS"
                            
                                                    
                                                               }
df.rename(columns=changes_in_column_names,
          inplace=True)

df["DATE"] = pd.to_datetime(df["DATE"],errors="coerce",dayfirst =True)
print(df["DATE"].isna().sum())
print(df.info())
print(df)

#fix dates with different fomart
mask =df["DATE"].astype(str).str.contains("-")
df.loc[mask,"DATE"]= pd.to_datetime(df.loc[mask, "DATE"], format="%Y-%m-%d",errors="coerce")

mask =df["DATE"].astype(str).str.contains("/")
df.loc[mask,"DATE"] =pd.to_datetime(df.loc[mask, "DATE"],format="%d/%m/%Y",errors= "coerce")

df["YEAR"]= df["DATE"].dt.year

#converting float to integer for the year column but first droping rows in NaN values can also chose to fill it,but will be droping it
df=df.dropna(subset=
             ["YEAR"])
df["YEAR"]= df["YEAR"].astype("Int64")

#NO MUCH CLEANING TO BE DONE YEAR DATA LOOKS GOOD SO MOVING ON TO EDA(EXPLORATORY DATA ANALYSIS)

#BUT FIRST I HAVE TO SAVE THE CLEANED VERSION 


#(saving as csv for sharing)
df.to_parquet("matches_cleaned_epl2023_data.csv")
#(saving as parquet for easy reloading)
df.to_parquet("matches_cleaned_epl2023_data.parquet", index=False)


