from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# KFold : sklearn에서 제공하는 모듈(모델)만 적용 가능
k_fold = KFold(n_splits = 10, shuffle = True, random_state = 0)

def getScore(clf): # clf : 모델의 인스턴스
    score = cross_val_score(clf, X_train, Y_train, cv = k_fold, 
                            n_jobs = 1, scoring = 'accuracy')
    return score

# 교차검증
scores = pd.DataFrame([
    getScore(KNeighborsClassifier(n_neighbors = 13)),
    getScore(DecisionTreeClassifier(random_state = 0)),
    getScore(RandomForestClassifier(n_estimators = 13, random_state = 0)),
    getScore(GaussianNB()),
    getScore(SVC(gamma = 'auto')),
    getScore(MLPClassifier(solver = 'sgd', activation = 'logistic',
                          hidden_layer_sizes = (48, 16),
                          random_state = 1, max_iter = 200000))],
    index = ['KNN', 'DT', 'RF', 'NB', 'SVM', 'MLP_s'])


scores['Mean'] = np.around(scores.mean(axis = 1)*100, 2)
scores
