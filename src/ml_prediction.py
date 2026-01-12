from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ml_predict_dropout_probability(df, feature_cols, target_col):
    X = df[feature_cols]
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    print("ML model accuracy:", accuracy_score(y_test, predictions))

    # Probability of FAIL (dropout)
    dropout_prob = probabilities[:, 0]

    return model, dropout_prob, X_test.index

"""
    Train a simple ML model to predict Pass/Fail.

    INPUTS:
        df : pandas.DataFrame
        feature_cols : list of str
            Column names to use as input features
        target_col : str
            Column name for target (e.g., Pass/Fail as 0/1)

    OUTPUTS:
        model : trained LogisticRegression model
        predictions : numpy array of predicted classes
    """