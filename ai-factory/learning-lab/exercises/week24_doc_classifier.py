#!/usr/bin/env python3
"""Week 24 — Document type classifier. pip install scikit-learn"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

DOCS = [
    ("ID", "national id card copy cmnd citizen"),
    ("ID", "passport biometric identity document"),
    ("CONTRACT", "loan agreement contract signature disbursement"),
    ("CONTRACT", "credit contract terms and conditions"),
    ("COLLATERAL", "motorbike registration collateral asset"),
    ("COLLATERAL", "vehicle ownership certificate lien"),
    ("OTHER", "customer service complaint ticket"),
    ("OTHER", "branch visit feedback survey"),
]
TEST = [
    ("ID", "identity card verification"),
    ("CONTRACT", "signed loan contract appendix"),
    ("COLLATERAL", "collateral motorbike pink book"),
]

X_train = [t for _, t in DOCS]
y_train = [l for l, _ in DOCS]
vec = CountVectorizer()
Xv = vec.fit_transform(X_train)
clf = LogisticRegression(max_iter=500).fit(Xv, y_train)

Xt = vec.transform([t for _, t in TEST])
yt = [l for l, _ in TEST]
acc = accuracy_score(yt, clf.predict(Xt))
print(f"Holdout accuracy: {acc:.1%} ({'PASS' if acc >= 0.8 else 'FAIL'} ≥80%)")
