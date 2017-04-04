# usr/bin/python2.7
# -*- coding:utf-8 *-

import numpy as np
import pandas as pd
import scipy as sp

data = pd.read_csv('gender_submission.csv')
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')



print data.columns
print train.columns
print test.columns


passengerId = train['PassengerId']
name = train['Name']
survived = train['Survived']
pclass = train['Pclass']
sex = train['Sex']
age = train['Age']
sibsp = train['SibSp']
parch = train['Parch']
ticket = train['Ticket']
fare = train['Fare']
cabin = train['Cabin']
embarked = train['Embarked']

def matrix(liste) :
	new = []
	for e in liste :
		e = e.as_matrix()
		new.append(e)
	return new

liste = [passengerId, name, survived, pclass, sex, age, sibsp, parch, ticket, fare, cabin, embarked]

liste = matrix(liste)

print passengerId
print name





data = data.as_matrix()
train = train.as_matrix()
test = test.as_matrix()

print train

"""data.shape()


train.shape()
test.shape()"""
