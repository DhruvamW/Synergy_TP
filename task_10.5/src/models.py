from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor



def train_dummy(X_train, X_val, y_train, y_val):
    model = DummyRegressor()
    model.fit(X_train,y_train)
    
    return model

def train_linear(X_train, X_val, y_train, y_val):
    model = LinearRegression()
    model.fit(X_train,y_train)
    
    return model

def train_ridge(X_train, X_val, y_train, y_val):
    model = Ridge()
    model.fit(X_train,y_train)
    
    return model

def train_tree(X_train, X_val, y_train, y_val):
    model = DecisionTreeRegressor()
    model.fit(X_train,y_train)
    
    return model

def train_forest(X_train, X_val, y_train, y_val):
    model = RandomForestRegressor()
    model.fit(X_train,y_train)
    
    return model
