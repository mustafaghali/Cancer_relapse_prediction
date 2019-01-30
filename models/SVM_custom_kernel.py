import data_reader
from sklearn.metrics import*
from sklearn.model_selection import train_test_split
from sklearn  import svm
import numpy as np

x, y = data_reader.read_data()

#x = (x-x.mean(axis = 0))/x.std(axis=0)
y = y.flatten()
x = x.T

for i in range (y.shape[0]):
    if y[i] == -1:
        y[i] =0


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)


def my_kernel(X, Y):

    return np.dot(X,Y.T)


h = .02  # step size in the mesh

# we create an instance of SVM and fit out data.
clf = svm.SVC(kernel=my_kernel)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred)

print(y_pred)
print("Accuracy: %.4f%%" % (accuracy * 100.0))

print("AUC %.4f%%" %(auc*100.0))
