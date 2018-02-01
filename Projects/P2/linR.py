import numpy as np
import timeit
from numpy import genfromtxt
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn import linear_model
from sklearn import tree
from sklearn.metrics import mean_absolute_error, mean_squared_error, matthews_corrcoef
from math import sqrt
from scipy.stats import pearsonr

raw_data = genfromtxt('processed.cleveland.csv', delimiter=',', missing_values="?", filling_values = (54.439, 0.68, 3.158, 131.69, 246.693, 0.149, 0.99, 149.607, 0.321, 1.04, 1.601, 0.672, 4.734, 0.937), skip_header=1)

X = raw_data[:, 1:]
y = raw_data[:, 0]

kf = KFold(n_splits=10)
kf.get_n_splits(X)

regr = linear_model.LinearRegression()

models = []

scores = cross_val_score(regr, X, y, cv=10)
#print("cross_val_score:", scores)    

#accuracy = scores.mean()
#stdev = scores.std()
#print("Accuracy: %0.2f"% accuracy)

regr.fit(X,y)

def fitlinR(regr, X, y):
    regr.fit(X,y)
    return regr

linRtime = timeit.timeit(lambda:fitlinR(regr, X, y), number=1)

print("LINEAR REGRESSION")
print("Time: ", linRtime)
print("Model:", regr.coef_)
print("intercept:", regr.intercept_)

y_pred = regr.predict(X)


pearsonR = pearsonr(y, y_pred)
print("Correlation Coefficient (Pearson):", pearsonR[0])

#mathewsR = matthews_corrcoef(y, y_pred)
#print("Correlation Coefficient (Matthews):", mathewsR)

mae = mean_absolute_error(y, y_pred)
print("Mean Absolute Error:", mae)

mse = mean_squared_error(y, y_pred)
rmse = sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("")

regtree = tree.DecisionTreeRegressor(min_samples_leaf=4)
smallerregtree = tree.DecisionTreeRegressor(min_samples_leaf=4, max_leaf_nodes = 6)

scores = cross_val_score(regtree, X, y, cv=10)

regtree.fit(X,y)

def fitRTree(regtree, X, y):
    regtree.fit(X,y)
    return regtree

rtreetime = timeit.timeit(lambda:fitRTree(regtree, X, y), number=1)
smallertime = timeit.timeit(lambda:fitRTree(smallerregtree, X, y), number = 1)

print("REGRESSION TREE")
print("Time: ", rtreetime)
print("Model:", regtree.tree_)
tree.export_graphviz(regtree, out_file='tree.dot')

y_pred = regtree.predict(X)

pearsonR = pearsonr(y, y_pred)
print("Correlation Coefficient (Pearson):", pearsonR[0])
mae = mean_absolute_error(y, y_pred)
print("Mean Absolute Error:", mae)

mse = mean_squared_error(y, y_pred)
rmse = sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("")

print("SMALLER REGRESSION TREE")
print("Time:", smallertime)
smallerregtree.fit(X,y)
tree.export_graphviz(smallerregtree, out_file='smalltree.dot')
y_pred = smallerregtree.predict(X)

pearsonR = pearsonr(y, y_pred)
print("Correlation Coefficient (Pearson):", pearsonR[0])
mae = mean_absolute_error(y, y_pred)
print("Mean Absolute Error:", mae)

mse = mean_squared_error(y, y_pred)
rmse = sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("")

print("ZeroR")
val = raw_data[:,0].mean()

def fitZeroR(raw_data, y):
    val = raw_data[:,0].mean()
    return y_pred

zeroRtime = timeit.timeit(lambda:fitZeroR, number=1)

print("Time:", zeroRtime)
print("Prediction: ", val)

y_pred = np.empty_like(y)
y_pred.fill(val)

pearsonR = pearsonr(y, y_pred)
print("Correlation Coefficient (Pearson):", pearsonR)

mae = mean_absolute_error(y, y_pred)
print("Mean Absolute Error:", mae)

mse = mean_squared_error(y, y_pred)
rmse = sqrt(mse)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)

