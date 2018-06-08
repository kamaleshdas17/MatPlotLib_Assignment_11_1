import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url='https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic=pd.read_csv(url)

#1. Create a pie chart presenting the male/female proportion
lavels=titanic.sex.dropna().unique()
x=titanic.groupby('sex').name.count()
#explode = (0.1, 0)

plt.style.use('classic')
plt.figure(figsize=(10,5))
plt.pie(x,labels=lavels,shadow=True,autopct='%1.1f%%',startangle=120,colors=['lightcoral','yellowgreen'])
plt.axis('equal')
plt.show()

#2. Create a scatterplot with the Fare paid and the Age, differ the plot color by gender
age=titanic.age
fare=titanic.fare
colors = np.where(titanic['sex']=='female','y','r')
plt.figure(figsize=(15,5))
plt.scatter(age,fare,c=colors,alpha=0.8)
#titanic.plot.scatter('age','fare',c=colors,alpha=0.8)
plt.xlabel('age')
plt.ylabel('fare')
plt.show()