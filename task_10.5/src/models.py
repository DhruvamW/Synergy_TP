from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from config import RANDOM_STATE



def train_dummy(X_train, y_train):
    model = DummyRegressor()
    model.fit(X_train,y_train)
    
    return model

def train_linear(X_train, y_train):

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression())
    ])

    pipeline.fit(X_train, y_train)

    return pipeline
    

def train_ridge(X_train, y_train):
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", Ridge())
    ])

    pipeline.fit(X_train, y_train)

    return pipeline 

def train_decision_tree(X_train, y_train):
    model = DecisionTreeRegressor(random_state=RANDOM_STATE)
    model.fit(X_train,y_train)
    
    return model

def train_random_forest(X_train, y_train):
    model = RandomForestRegressor(random_state=RANDOM_STATE)
    model.fit(X_train,y_train)
    
    return model
