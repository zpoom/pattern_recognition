import pandas as pd
import numpy as np
import math
from google.colab import drive
drive.mount('drive')

def logistic_fnc(data,theta):
  return 1/(1+math.e**(-1*np.dot(theta.T,data.T)))

train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)
test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)
train["Age"] = train["Age"].fillna(train["Age"].median())
train.loc[train["Embarked"] == "S", "Embarked"] = 0
train.loc[train["Embarked"] == "C", "Embarked"] = 1
train.loc[train["Embarked"] == "Q", "Embarked"] = 2
train.loc[train["Sex"] == "male", "Sex"] = 0
train.loc[train["Sex"] == "female", "Sex"] = 1
train["Sex"] = train["Sex"].fillna(train["Sex"].mode()[0])
train["Embarked"] = train["Embarked"].fillna(train["Embarked"].mode()[0])
test["Age"] = test["Age"].fillna(test["Age"].median())
test.loc[test["Embarked"] == "S", "Embarked"] = 0
test.loc[test["Embarked"] == "C", "Embarked"] = 1
test.loc[test["Embarked"] == "Q", "Embarked"] = 2
test["Embarked"] = test["Embarked"].fillna(test["Embarked"].mode()[0])
test.loc[test["Sex"] == "male", "Sex"] = 0
test.loc[test["Sex"] == "female", "Sex"] = 1
test["Sex"] = test["Sex"].fillna(test["Sex"].mode()[0])
test_data = np.array(test[["Pclass","Sex","Age","Embarked"]].values,dtype = float)
test_id = np.array(test[["PassengerId"]].values)
# print(test)
x = np.array(train[["Pclass","Sex","Age","Embarked"]].values,dtype = float)
t = np.ones((x.shape[0],1),dtype=float)
x = np.append(x,t,axis=1)
y = np.array(train[["Survived"]].values,dtype = float)
r = 0.0001
theta = np.ones((5,),dtype=float)
for k in range(200000):
  for j in range(x.shape[1]):
    sm = float(0)
#     print("sm1 :"+str(sm))
    for i in range(x.shape[0]):
#       print(i,j,k)
#       print(str(x[[i],:].T) +" "+str(theta.T))
#       print(type(x[i,j]))
#       print(i,j)
#       print("val "+str(float(float(y[i,0]) - float(logistic_fnc(x[i,:],theta))) * float(x[i,j])))
      sm += float(float(y[i,0]) - float(logistic_fnc(x[i,:],theta))) * float(x[i,j])
#       print("sm "+str(sm))
    theta[j,] += float(sm*r)
#     print(theta)
#print(theta)
# print(theta[:4,].shape)
# print(test_data.shape)
# print(np.dot(theta[:4,].T,test_data.T))
tmp = logistic_fnc(test_data,theta[:4,])
# print(ans)
#print(ans.shape)
ans = np.ones((tmp.shape[0],2),dtype=int)
for i in range(tmp.shape[0]):
  ans[i,0] = int(892+i)
  if tmp[i] >= 0.5: 
    ans[i,1] = 1
  else : 
    ans[i,1] = 0
out = pd.DataFrame(data=ans,columns=["PassengerId","Survived"])
out.to_csv("patternhw1.csv",index=False)
!cp patternhw1.csv drive/My\ Drive/
  
