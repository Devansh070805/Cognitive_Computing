 import numpy as np

X = sum(ord(c) for c in 'DK')  

sales = np.array([X, X+50, X+100, X+150, X+200])
tax_rate = ((X % 5) + 5) / 100
taxed_sales = sales * (1 + tax_rate)

discounted_sales = np.where(sales < X+100, sales * 0.95, sales * 0.90)

weeks_sales = np.vstack([sales, sales * 1.02, sales * 1.04])
print(weeks_sales)
