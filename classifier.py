import joblib

model, vectorizer = joblib.load("models/role_classifier.pkl")

def predict_role(text):
    X = vectorizer.transform([text])
    role = model.predict(X)[0]
    score = model.predict_proba(X).max()
    return role, round(score*100,2)
