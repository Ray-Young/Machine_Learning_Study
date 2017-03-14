import numpy as np
import csv

def read_file(file):
    X = []
    with open(file) as f:
        for line in f:
            item = line.strip().split(',')
            item = [float(i) for i in item]
            X.append(item)
    return np.asarray(X)

def group_training_data(X):
    y = X[:, [len(X[0]) - 1]]
    y = np.reshape(y, -1)
    return np.asarray(y)

def handler(X, y, source, k, file2):
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.neighbors import NearestNeighbors
    neigh = KNeighborsClassifier(n_neighbors=int(k), p=2,
metric='minkowski')
    nearest_neigh = NearestNeighbors(n_neighbors=1, p=2,
metric='minkowski')

    neigh.fit(X, y)
    nearest_neigh.fit(X)
    f = open(file2, 'w')
    datawriter = csv.writer(f, delimiter=',')
    for i in source:
        item = np.asarray(i).reshape(1, -1)
        result = []
        result.append(nearest_neigh.kneighbors(item,
return_distance=False)[0][0] + 1)
        result = np.append(result, item)
        result = np.append(result, neigh.predict(item)[0])
        datawriter.writerow(result)
        string = ','.join([str(i) for i in result])
        print(string)
    f.close()

def run(k, file1, file2):
    X = read_file(file1)
    y = group_training_data(X)
    source = read_file(file2)
    handler(X, y, source, k, file2)
