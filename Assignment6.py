#Q1
import numpy as np
import matplotlib.pyplot as plt
M = float(input("Enter M: "))
x = np.linspace(-10, 10, 100)
y1 = M*x**2
y2 = M*np.sin(x)
plt.plot(x, y1, 'r--', label='y = Mx^2')  
plt.plot(x, y2, 'b-', label='y = Msin(x)')  
plt.legend()
plt.grid(True)
plt.title(f"Plot of y = Mx² and y = Msin(x) for M={M}")
plt.show()

#Q2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "Subject": ["Math", "Science", "English", "History", "Art"],
    "Score": [34,88,68,88,97]
}
df = pd.DataFrame(data)
ax = sns.barplot(x="Subject", y="Score", data=df, palette="husl") 
for i, score in enumerate(df["Score"]):
    ax.text(i, score + 1, str(score))
plt.title("Scores by Subject")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.ylim(0, 100) 
plt.grid(axis='y', linestyle="--", alpha=0.7)  
plt.show()

#Q3
np.random.seed(102317243)
data=np.random.randn(50)
plt.subplot(2,2,1)
plt.plot(np.cumsum(data),color='blue')
plt.title('Cumulative sum')
plt.xlabel('Sum')
plt.ylabel('Cumulative value')
plt.grid(True)
plt.subplot(2,2,2)
x=np.arange(50)
y=data+np.random.normal(scale=0.5,size=50)
plt.scatter(x,y,color='green')
plt.title('Scatter plot with noise')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.show()

#Q4
dataset= 'https://github.com/AnjulaMehto/MCA/raw/main/company_sales_data.csv'
df=pd.read_csv(dataset)
sns.lineplot(x=df['month_number'],y=df['total_profit'],marker='o',color='blue')
plt.title('Total profit over months')
plt.xlabel('Month number')
plt.ylabel('Total profit')
plt.grid(True)
plt.show()
for column in df.columns[1:-1]:
  sns.lineplot(x=df['month_number'],y=df[column],label=column)
plt.title('Product Sales over Month')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()
df.sum().drop('month_number').plot(kind='bar',color='blue')
plt.title('Total Sales and profit by feature')
plt.xlabel('Features')
plt.ylabel('Total Values')
plt.grid(True,linestyle='--',alpha=0.7)
plt.show()