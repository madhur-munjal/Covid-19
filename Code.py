import pandas as pd

df = pd.read_csv(r'covid_time2703.csv')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Madhur\Desktop\covid_time2703.csv')

# df = df.groupby('Country/Region').sum()

x = df.iloc[:,1:2]
y = df.iloc[:,43:]

df1 = pd.concat([x,y],axis = 1).set_index('Country/Region')
df1 = df1.groupby('Country/Region').sum()
df1 = df1.T
# df1['Country/Region'] = df['Country/Region'][:-2]
# df1

for i in df['Country/Region'].unique():
    country = i
    plt.plot(df1.index,df1[country], label = country)
    plt.xticks(rotation = 90)
    plt.tick_params(axis = 'both', which = 'major', labelsize = 8)
    plt.legend(loc="upper left")
    plt.show()
