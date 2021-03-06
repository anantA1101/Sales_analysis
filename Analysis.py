import pandas as pd
import os 
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#Task1: merge data folders of 12 months
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************

path="D:\DATA SCIENCE PROJECTS\data\sales_data\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data"
#df =pd.read_csv("D:\DATA SCIENCE PROJECTS\data\sales_data\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data\Sales_April_2019.csv")

""" files= [file for file in os.listdir(path)]

all_months_data= pd.DataFrame()          # to create a new dataframe

for file in files:
    df = pd.read_csv( 'D:\DATA SCIENCE PROJECTS\data\sales_data\Pandas-Data-Science-Tasks-master\SalesAnalysis\Sales_Data/' + file)
    all_months_data= pd.concat([all_months_data, df])

all_months_data.to_csv("all_data.csv" , index=False) """

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#Task1: Read the new data
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
all_data = pd.read_csv("all_data.csv")
#print(all_data.head())
#************************************************************************************************************************************************************************
#********************************************************CLEAN THE DATA****************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#Drop NAN
all_data = all_data.dropna(how="all")

#Filter Or
all_data = all_data[all_data["Order Date"].str[0:2] != 'Or' ]

#convert str to int and float 
all_data['Quantity Ordered'] = all_data["Quantity Ordered"].astype("int32")
all_data['Price Each'] = all_data["Price Each"].astype("float")




#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#Task1: What was the best month for sales and how much was earned that month
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************

#sub task : add data with additional columns 

#MONTH COLUMN
all_data['Month'] = all_data["Order Date"].str[0:2]
all_data['Month'] = all_data["Month"].astype("int32")
#print(all_data.head())

#Sales Column 
all_data["Sales"] = all_data["Quantity Ordered"] * all_data["Price Each"]
#print(all_data.head())


results= all_data.groupby("Month").sum()

#Plotting

""" months= range(1,13)
plt.bar(months,results['Sales'])
plt.xticks(months)
plt.xlabel("Months ")
plt.ylabel("sales in US dollars")
plt.show() """

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#Task1: What was the best month for sales and how much was earned that month(USING APPLY METHOD)
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
def get_city(adress):
    return adress.split(",")[1]

def get_state(adress):
    return adress.split(",")[2].split(" ")[1]


all_data["City"]= all_data["Purchase Address"].apply(lambda x : get_city(x) + " " +get_state(x))

results = all_data.groupby("City").sum()
#print(results)

cities= [city for city,df in all_data.groupby('City')]           #********************************************************************************

""" plt.bar(cities,results['Sales'])
plt.xticks(cities, size=6)
plt.xlabel("cities")
plt.ylabel("sales in the cities ")
plt.show() """


#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
                  #What time should we display the advertizements to maximize likelyhood of customers buying products
#************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
""" 
all_data["Order Date"] = pd.to_datetime(all_data["Order Date"])

all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute

hours= [h for h, df in all_data.groupby('Hour')] """

""" plt.plot(hours,all_data.groupby('Hour').count())
plt.xticks(hours)
plt.xlabel("Hours")
plt.ylabel("Number of Orders")
plt.grid()
plt.show()
print(all_data.groupby('Hour')) """

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
                  #What city sold most Product
#************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
all_data.groupby(['City']).sum()

keys = [city for city, df in all_data.groupby(['City'])]

plt.bar(keys,all_data.groupby(['City']).sum()['Sales'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('City')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
                  #What products are most often sold together
#************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
""" df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df2 = df[['Order ID', 'Grouped']].drop_duplicates()


count = Counter()

for row in df2['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 2)))

for key,value in count.most_common(10):
    print(key, value) """

#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
#************************************************************************************************************************************************************************
                  #What product sold the most? Why do you think it sold the most
#************************************************************************************************************************************************************************
#***********************************************************************************************************************************************************************
#************************************************************************************************************************************************************************

""" product_group = all_data.groupby('Product')
quantity_ordered = product_group.sum()['Quantity Ordered']

keys = [pair for pair, df in product_group] """
""" plt.bar(keys, quantity_ordered)
plt.xticks(keys, rotation='vertical', size=8)
plt.show() """


""" prices = all_data.groupby('Product').mean()['Price Each']

fig, ax1 = plt.subplots()


ax2 = ax1.twinx()
ax1.bar(keys, quantity_ordered, color='b')
ax2.plot(keys, prices, color='r')

ax1.set_xlabel('Product Name')
ax1.set_ylabel('Quantity Ordered', color='b')
ax2.set_ylabel('Price ($)', color='r')
ax1.set_xticklabels(keys,rotation= 90,  size=6)


plt.show()
 """