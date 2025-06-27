import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url="C:/ml project 1/sales.txt"
df = pd.read_csv(url, sep='\t', header=None)
print(df.head())
df.columns=['sales','advertisement']

x=df['sales'].values
y=df['advertisement'].values

x = x.reshape(-1,1)
y = y.reshape(-1,1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(x_train,y_train)
y_pred=lm.predict(x_test)

a = lm.coef_
b = lm.intercept_,
print("Estimated model slope, a:" , a)
print("Estimated model intercept, b:" , b) 

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print("RMSE value: {:.4f}".format(rmse))

from sklearn.metrics import r2_score
print ("R2 Score value: {:.4f}".format(r2_score(y_test, y_pred)))

plt.scatter(x, y, color = 'blue', label='Scatter Plot')
plt.plot(x_test, y_pred, color = 'black', linewidth=3, label = 'Regression Line')
plt.title('Relationship between Sales and Advertising')
plt.xlabel('Sales')
plt.ylabel('Advertising')
plt.legend(loc=4)
plt.show()

