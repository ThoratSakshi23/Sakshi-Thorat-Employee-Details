import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

#Load Excel File
df=pd.read_excel("Excel_file.xlsx")
print(df)

#DATA CLEANING

#check for missing values:
file_path="Excel_file.xlsx"
print("Check for The Missing Values.....:")
def missing(file_path):
    print(df.isnull().sum())
     
missing(file_path)

#Fill  null values:
def operation(df):
    if df.isnull().values.any():
        df = df.fillna(0)
        print("Filled missing values with 0:")
    else:
        print("No missing values to fill.")
    print(df)

operation(df)

#drop Null Values:
def drop(df):
    if df.isnull().values.any():
        df = df.dropna()
        print("Dropped rows containing NULL values:")
    else:
        print("No rows dropped ")
    print(df)
drop(df)


#Remove duplicates rows:
def Remove(df):
    print("Remove The Duplicates Rows.....:") 
    print(df.drop_duplicates())
    
Remove(df)

#Rename or Format column names:
print("Rename or Format Column Names.....:")
coln=df.columns.str.strip().str.lower()
print(coln)

#change data types:
print("Change The Data Types.....:")
data=df['Salary'].astype(int)
print(data)

#data Analysis

#Find Average
def Average(df):
    print("The Average salary is.....:")
    salary_mean=df['Salary'].mean()
    print(salary_mean)
Average(df)    

#Find Maximum
def Max(df): 
    print("The Maximum Salary.....:")
    salary_max=df['Salary'].max()
    print(salary_max)
Max(df)

#Find Minimum
def Min(df):
    print("The Minimum salary.....:")
    Salary_min=df['Salary'].min()
    print(Salary_min)
Min(df)

#Value counts of Categories:
def Counts(df):
    print("Value Counts of Categories.....:")
    value=df['Emp_dept'].value_counts()
    print(value)
Counts(df)

#Filter data with condition:
print("Filter Data With Condition.....:")
con=df[df['Salary']>75000]
print(con)

# Sort The Data :
print("Sort The Data.....:")
df.sort_values(by='Salary', ascending=False)
print(df)

#Create Charts(Data Visualization)

#Barplot

sns.barplot(x='Emp_dept',y='Salary',data=df)
plt.title("Department Wise Average  Salary " )
plt.show()          

#ScatterPlot:
sns.scatterplot(x='Age',y='Salary',data=df)
plt.title("Age Vs Salary With Deperatment ")
plt.show()



