import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


roll_number = 102317122  
np.random.seed(roll_number)


sales_data = np.random.randint(1000, 5001, size=(12, 4))


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
categories = ["Electronics", "Clothing", "Home & Kitchen", "Sports"]
sales_df = pd.DataFrame(sales_data, columns=categories, index=months)


print(sales_df.head())
print(sales_df.describe())

total_sales_category = sales_df.sum()

sales_df["Total Sales"] = sales_df.sum(axis=1)

sales_growth = sales_df[categories].pct_change().mean()

sales_df["Growth Rate"] = sales_df["Total Sales"].pct_change() * 100

if roll_number % 2 == 0:
    sales_df["Electronics"] *= 0.9  
else:
    sales_df["Clothing"] *= 0.85 


plt.figure(figsize=(10, 6))
for category in categories:
    plt.plot(sales_df.index, sales_df[category], label=category)
plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trends")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(data=sales_df[categories])
plt.title("Sales Distribution Per Category")
plt.show()

array = np.array([[1, -2, 3], [-4, 5, -6]])
absolute_values = np.abs(array)
percentiles = {
    "Flattened": np.percentile(array, [25, 50, 75]),
    "Columns": np.percentile(array, [25, 50, 75], axis=0),
    "Rows": np.percentile(array, [25, 50, 75], axis=1)
}
mean = np.mean(array, axis=None)
median = np.median(array, axis=None)
std_dev = np.std(array, axis=None)

arr = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])
floor_vals = np.floor(arr)
ceil_vals = np.ceil(arr)
trunc_vals = np.trunc(arr)
rounded_vals = np.round(arr)

lst = [1, 2, 3, 4, 5]
temp = lst[1]
lst[1] = lst[3]
lst[3] = temp

s = {10, 20, 30, 40, 50}
lst_s = list(s)
lst_s[0], lst_s[2] = lst_s[2], lst_s[0]
s = set(lst_s)

