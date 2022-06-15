### Measure of Similarity

# 1. Jaccard Similarity
from math import *
 
def jaccard_similarity(x, y):
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    
    return intersection_cardinality / float(union_cardinality)
 
print(jaccard_similarity(['A', 'B', 'C', 'D'],['A', 'C', 'F', 'G']))



# 2. Cosine Similarity
### 함수 만들기
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * (np.linalg.norm(b)))

print(cosine_similarity([3, 10, 7, 2], [2, 15, 10, 12]))

### 내장함수 이용하기
from scipy.spatial.distance import cosine
# cosine : 거리 계산
print(1 - cosine([3, 10, 7, 2], [2, 15, 10, 12]))



# 3. Pearson Similarity
### 함수 생성 / pearsonr in scipy / corrcoef in numpy
from scipy.stats import pearsonr

def pearson_similarity(a, b):
    return np.dot((a - np.mean(a)), (b - np.mean(b))) / ((np.linalg.norm(a - np.mean(a))) * (np.linalg.norm(b - np.mean(b))))

display(pearson_similarity([3, 10, 7, 2], [2, 15, 10, 12])
       , pearsonr([3, 10, 7, 2], [2, 15, 10, 12])
       , np.corrcoef([3, 10, 7, 2], [2, 15, 10, 12]))
