import pandas as pd

data = {
    'Tid': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Refund': ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    'Marital Status': ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    'Taxable Income': ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    'Cheat': ["No", "No", "No", "No", "Yes", "No", "Yes", "No", "No", "Yes"]
}

df = pd.DataFrame(data)
print(df)


selected_rows = df.loc[[0, 4, 7, 8]]
print("Rows 0, 4, 7, and 8:")
print(selected_rows)


rows_3_to_7 = df.iloc[3:8] 
print("Rows from index 3 to 7:")
print(rows_3_to_7)


subset_rows_cols = df.iloc[4:9, 2:5]  
print("\nRows 4 to 8 and columns 2 to 4:")
print(subset_rows_cols)


columns_1_to_3 = df.iloc[:, 1:4] 
print("\nAll rows with column index 1 to 3:")
print(columns_1_to_3)

content=pd.read_csv("example.csv")
print(content.head())

content=content.drop(index=4)
content=content.drop(content.columns[3],axis=1)


data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5],
}

df = pd.DataFrame(data)


shape = df.shape

summary = df.info()
stats = df.describe()


first_five = df.head()
last_three = df.tail(3)


average_salary = df["Salary"].mean()
total_bonus = df["Bonus"].sum()
youngest_age = df["Age"].min()
highest_rating = df["Rating"].max()

sorted_df = df.sort_values(by="Salary", ascending=False)


df["Performance_Category"] = pd.cut(
    df["Rating"], [0, 4.0, 4.5, float("inf")], labels=["Average", "Good", "Excellent"]
)

missing_values = df.isnull().sum()


df.rename(columns={"Employee_ID": "ID"}, inplace=True)

filtered_employees = df[(df["Years_of_Experience"] > 5) & (df["Department"] == "IT")]

df["Tax"] = df["Salary"] * 0.1

df.to_csv("modified_employees.csv", index=False)
