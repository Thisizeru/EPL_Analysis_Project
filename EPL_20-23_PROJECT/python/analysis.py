# =================================================
# EPL 2020-2023 DATA ANALYIS PROJECT
# Author: Paul Eru
# Purpose: Analyze EPl data to find key insights
# ============================================ 


# -----------------------
# 1. Importing Libraries 
#------------------------
import pandas as pd
import pyarrow

#----------------------------------------------
# 2.importing the cleaned version of the data
#-----------------------------------------------

df=pd.read_parquet("EPL_20-23_PROJECT\Epl21_23_datasets\matches_cleaned_epl21_23_data.parquet")
print(df)


#------------------------------------------------------------
# 3.EXPLORATORY DATA ANALYSIS(EDA) & A LITTLE SEASONAL INSIGHTS
#-------------------------------------------------------------


total_goals= df["HOME TEAM GOALS"]+df["AWAY TEAM GOALS"].sum()

print(total_goals)


#---------------------------------------------------------------------------------
# 4.ADDING IT TO THE DATFRAME AS A COLUMN FOR BETTER UNDERSTANDING AND VISUALIZATION 
#--------------------------------------------------------------------------------
df["TOTAL GOALS"] =df["HOME TEAM GOALS"]+df["AWAY TEAM GOALS"]
print(df.info())

#------------------------------
# 5.checking for per team goals
#-------------------------------

home_goals=df.groupby("HOME TEAM")["HOME TEAM GOALS"].sum()
print(home_goals)

away_goals= df.groupby("AWAY TEAM")["AWAY TEAM GOALS"].sum()

print(away_goals)

#MATCH OUTCOMES INSIGHT
#--------------------------------------------------------------
# 6.checking for match results against home team and away team
#--------------------------------------------------------------
def match_results(row):
    if row ["HOME TEAM GOALS"]>row["AWAY TEAM GOALS"]:
        return "Home win"
    elif row["HOME TEAM GOALS"] <row["AWAY TEAM GOALS"]:
        return "Away win"
    else:
        return "Draw"

df["match_results"] = df.apply(match_results,axis=1)

print(df.columns)

#-------------------------------------------------------------
#7.renaming the new column in capital letters just like others
#-------------------------------------------------------------
changes={
    "match_results":"MATCH RESULTS"
    }
print(df.rename(
                  columns=changes
               )
               ) 

#checking final result of EDA 3
print(df[["HOME TEAM GOALS",
           "AWAY TEAM GOALS",
            "match_results" ]])

#-----------------------
# 8.DISCIPLINE ANALYSIS
#------------------------
total_fouls_committed=df["HOME FOULS"] +df["AWAY FOULS"]
print(total_fouls_committed)


yellow_cards= df["HOME YELLOW CARDS"] + df["AWAY YELLOW CARDS"].sum()
red_cards= df["HOME RED CARDS"] + df["AWAY RED CARDS"].sum()
total_number_of_cards=["yellow_cards"] + ["red_cards"]
print("total_number_of_cards")

#------------------
# 9.Goals per year
#-------------------

#-----------------------------------------------------------------
#To calculate goals per year for a little matplotlib and seaborn
#------------------------------------------------------------------
goals_per_year=df.groupby("YEAR")[["HOME TEAM GOALS","AWAY TEAM GOALS"]].sum()
print(goals_per_year)

#importing matplotlib and seaborn though will be using only matplotlib for now
import matplotlib.pyplot as plt

goals_per_year.plot(kind="bar",figsize =(8,5))
plt.title("Total Goals Per Year")
plt.ylabel("Goals")
plt.xlabel("year")
plt.show()

#saving 

plt.savefig("goals_per_year.png")


#--------------------------------
#10.Average attendance per stadium
#--------------------------------
#Attendance = df.groupby("STADIUM")["ATTENDANCE"].mean()
#print(Attendance.head(10))
# the above code did not work because the ATTENDANCE column is an object datatype

#11.converting ATTENDANCE column to float and removing commas to find the average attendance per stadium
df["ATTENDANCE"] = df["ATTENDANCE"].replace(",","", regex =True).astype(float)
attendance =df.groupby("STADIUM")["ATTENDANCE"].mean()
print(attendance)

#--------------------------------------------
#visualizing  average attendance per stadium
#-------------------------------------------- 
attendance.head(10).plot(kind="bar", figsize=(10,5))
plt.title("Top Stadiums By Average Atendance")
plt.ylabel("Average Attendance")
plt.xlabel("Stadium")
plt.show()
plt.savefig("Top_Stadiums_By_Average_Atendance")

#------------------------------------------------------------------------------
#saving the analyzed dataset so as to load into postgres,cause of the columns
#------------------------------------------------------------------------------

#(saving as csv file for sharing)
#df.to_csv("matches_analyzed_epl2023.csv") 
#(saving as parquet for reloading into postgres database for further queries and additions of vital columns)
#df.to_parquet("matches_analyzed_epl2023.parquet")
#df=pd.read_parquet("matches_analyzed_epl2023.parquet")
print(df.head(10))
print(df.dtypes)

df["ATTENDANCE"] = df["ATTENDANCE"].replace(",","", regex =True).astype(float)
attendance =df.groupby("STADIUM")["ATTENDANCE"].sum().nlargest()
print(attendance)
