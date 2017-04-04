import numpy as np
import pandas as pd
import scipy as sp
from sklearn import neighbors, metrics, model_selection

data = pd.read_csv('gender_submission.csv')
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

data.head()
train.head()
test.head()

survivors = train['Survived']
train = train.drop('Survived', axis=1)
train.head()



survivors.describe()
survivors.astype('int')
survivors.unique()

train['Pclass'].describe()
train['Pclass'].astype('int')
train['Pclass'].unique()
train['Pclass'].isnull().any()

train['Name'].describe()
train['Name'].astype('str')
train['Name'].duplicated().unique()
(train['Name'].value_counts() > 1).any()
train['Name'].isnull().any()

train['Sex'].unique()

train['Age'].between(0,99).all()
train['Age'].notnull().unique()
train['Age'].value_counts()
train['Age'].astype(int)

clean_train = train[train['Cabin'].notnull() & train['Age'].between(0,99)]

%matplotlib inline
train['Age'].hist()


clean_train = train[train['Embarked'].notnull() & train['Cabin'].notnull() & train['Age'].notnull()].copy()

clean_train.notnull().all().all()

clean_train['Age'] = clean_train['Age'].astype('int')

clean_train.set_index('PassengerId')
clean_train['Sex'] = clean_train['Sex'].map({'male': 0, 'female': 1})
clean_train['Sex'].hist()
clean_train['Sex'].unique()
clean_train['Pclass'].hist()
