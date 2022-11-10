import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection  import  train_test_split 
from sklearn.model_selection  import StratifiedShuffleSplit 
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor




#loading data----------------------------------------------------------------
housing = pd.read_csv("databestop.csv")



# spliting data
split = StratifiedShuffleSplit(n_splits= 1 ,test_size= 0.2 , random_state= 42)
for train_index , test_index in split.split(housing,housing["CHAS"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]


# from training data we seperate price and all data
housing = strat_train_set.drop("MEDV     ",axis =1)
housing_label = strat_train_set["MEDV     "].copy()

#using pipeline for misising data and standerised data
my_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")), # we can use more function
    ("std_scaler", StandardScaler())
])
housing_num_tr = my_pipeline.fit_transform(housing)




# usig diff model to find best model ------------------------
#model = LinearRegression()
#model = DecisionTreeRegressor()
model= RandomForestRegressor()
model.fit(housing_num_tr, housing_label)




# using this we can find mean squred error
housing_predicts = model.predict(housing_num_tr)
mse = mean_squared_error(housing_label,housing_predicts)
rmse = np.sqrt(mse)
print(rmse)







# if mean squred error is zero we need to use cross validition
scores = cross_val_score(model,housing_num_tr,housing_label , scoring= "neg_mean_squared_error", cv =10)
rmse_score = np.sqrt(-scores)
print(rmse_score)


# using the test data
housing = strat_test_set.drop("MEDV     ",axis =1)
housing_label = strat_test_set["MEDV     "].copy()
my_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")), # we can use more function
    ("std_scaler", StandardScaler())
])
housing_num_tr = my_pipeline.fit_transform(housing)


housing_predicts = model.predict(housing_num_tr)
print(housing_predicts, list(housing_label))

mse = mean_squared_error(housing_label,housing_predicts)
rmse = np.sqrt(mse)
print(rmse)