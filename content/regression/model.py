from sklearn.linear_model import LinearRegression

def linreg(X_train, X_test, y_train, y_test):
    lm = LinearRegression()
    lm.fit(X_train, y_train)
    y_pred_train = lm.predict(X_train)
    y_pred_test = lm.predict(X_test)
    return y_pred_train, y_pred_test