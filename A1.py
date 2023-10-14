import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

def preprocessing():
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    print("df: ", df)
    labels = df['target']
    df.drop(columns=['target'], inplace=True)
    xtrain, xtest, ytrain, ytest = train_test_split(
        df, labels, test_size=0.3, random_state=42
    )
    ytrain = ytrain.values.ravel()
    ytest = ytest.values.ravel()
    return xtrain, xtest, ytrain, ytest

xtrain, xtest, ytrain, ytest = preprocessing()

def train_and_evaluate_random_forest(
    xtrain, ytrain, xtest, ytest, n_estimators=10, random_state=42
):
    RF = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
    RF.fit(xtrain, ytrain)
    ypred_rf = RF.predict(xtest)
    acc_rf = accuracy_score(ytest, ypred_rf) * 100
    f1_rf = f1_score(ytest, ypred_rf, average='macro') * 100
    return acc_rf, f1_rf

# Example usage:
acc_rf, f1_rf = train_and_evaluate_random_forest(xtrain, ytrain, xtest, ytest)
print("Random Forest Classifier Metrics:")
print("Accuracy: ", acc_rf)
print("F1 Score: ", f1_rf)
