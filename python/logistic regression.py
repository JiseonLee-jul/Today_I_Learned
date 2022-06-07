##### Logistic regression
from sklearn.preprocessing import minmax_scale
from sklearn.feature_selection import RFECV

# feature selection : RFE(Backward elimination)
X_train = train.iloc[:,3:]
Y_train = train['성별코드']

X_train_scaled = minmax_scale(X_train)

rfecv = RFECV(estimator = LogisticRegression(), step = 1, cv = 10, scoring = 'accuracy')
rfecv.fit(X_train_scaled, Y_train)

print("Optimal number of features: %d" % rfecv.n_features_)
print('Selected features: %s' % list(X_train.columns[rfecv.support_]))

# Plot number of features VS. cross-validation scores
plt.figure(figsize=(10,6))
plt.plot(range(1, len(rfecv.grid_scores_) + 1), rfecv.grid_scores_)
plt.xlabel("Number of features selected")
plt.ylabel("Cross validation score (nb of correct classifications)")
plt.show()

# logistic regression using selectted features
from sklearn.metrics import accuracy_score 

selected_features = ['성별코드', '신장(5Cm단위)', '체중(5Kg단위)', '허리둘레', 
                      '시력(좌)', '청력(좌)', '청력(우)', '수축기혈압', '이완기혈압', 
                      '식전혈당(공복혈당)', '총콜레스테롤', 'HDL콜레스테롤', 'LDL콜레스테롤', 
                      '혈색소', '혈청크레아티닌', '(혈청지오티)AST', '감마지티피', '흡연상태', 
                      '실명', 'WHtR', '비만여부', 'HDL콜레스테롤_bi']
X = train_final.iloc[:,1:]
X_scaled = minmax_scale(X)
y = train_final['성별코드']
X_test_scaled = minmax_scale(test[selected_features].iloc[:,1:])

# check classification scores of logistic regression
logreg = LogisticRegression()
logreg.fit(X_scaled, y)
y_pred = logreg.predict(X_test_scaled)
y_pred_proba = logreg.predict_proba(X_test_scaled)[:, 1]

print("Logistic regression accuracy is %2.3f" % accuracy_score(test['성별코드'], y_pred))
pd.DataFrame(zip(X.columns, logreg.coef_.ravel()), columns = ['feature', 'coef']).sort_values('coef', ascending = False)

