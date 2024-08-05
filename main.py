import pandas as pd
from sklearn.ensemble import RandomForestRegressor

train = pd.read_csv('vehicles.csv')

train.head()

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


train['DateTime'] = train['DateTime'].map(pd.to_datetime)
train['date'] = train['DateTime'].map(get_dom)
train['weekday'] = train['DateTime'].map(get_weekday)
train['hour'] = train['DateTime'].map(get_hour)
train['month'] = train['DateTime'].map(get_month)
train['year'] = train['DateTime'].map(get_year)
train['dayofyear'] = train['DateTime'].map(get_dayofyear)
train['weekofyear'] = train['DateTime'].map(get_weekofyear)

train.head()

train = train.drop(['DateTime'], axis=1)

train1 = train.drop(['Vehicles'], axis=1)

target = train['Vehicles']

print(train1.head())
target.head()

m1=RandomForestRegressor()
 
m1.fit(train1,target)
m1.predict([[5,30,8,19,2003,17,4]])