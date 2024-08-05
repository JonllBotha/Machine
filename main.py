import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = pd.read_csv('vehicles.csv')

def get_dom(dt):
	return dt.day

def get_weekday(dt):
	return dt.weekday()

def get_hour(dt):
	return dt.hour

def get_year(dt):
	return dt.year

def get_month(dt):
	return dt.month

def get_dayofyear(dt):
	return dt.dayofyear

def get_weekofyear(dt):
	return dt.weekofyear


data['DateTime'] = data['DateTime'].map(pd.to_datetime)
data['date'] = data['DateTime'].map(get_dom)
data['weekday'] = data['DateTime'].map(get_weekday)
data['hour'] = data['DateTime'].map(get_hour)
data['month'] = data['DateTime'].map(get_month)
data['year'] = data['DateTime'].map(get_year)
data['dayofyear'] = data['DateTime'].map(get_dayofyear)
data['weekofyear'] = data['DateTime'].map(get_weekofyear)

data.head()

data = data.drop(['DateTime'], axis=1)

data1 = data.drop(['Vehicles'], axis=1)

target = data['Vehicles']

print(data1.head())
target.head()

d1=RandomForestRegressor()
 
d1.fit(data1,target)
d1.predict([[5,30,8,19,2003,17,4]])