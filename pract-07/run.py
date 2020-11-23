import numpy 
import scipy.io
from displayData import displayData
from predict import predict
import matplotlib.pyplot as plt

# ЗАДАНИЕ №1
test_set = scipy.io.loadmat('test_set.mat')
weights = scipy.io.loadmat('weights.mat')

# ЗАДАНИЕ №2
X = test_set['X']
y = numpy.int64(test_set['y'])
Theta1 = weights['Theta1']
Theta2 = weights['Theta2']
m = X.shape[0]

# ЗАДАНИЕ №3
Index = numpy.random.permutation(m)
k = numpy.zeros((100,X.shape[1]))
for i in range(100):
    k[i] = X[Index[i]]
displayData(k)

# ЗАДАНИЕ №6
pre = predict(Theta1, Theta2, X)
y.ravel()
a = (pre == y.ravel())
print(a)
result = numpy.mean(numpy.double(a))
print(result)

# ЗАДАНИЕ №7
rp = numpy.random.permutation(m)
plt.figure()
for i in range(5):
    X2 = X[rp[i],:]
    X2 = numpy.matrix(X[rp[i]])
    pred = predict(Theta1, Theta2, X2.getA())
    pred = numpy.squeeze(pred)
    pred_str = 'Neural Network Prediction: %d (digit %d)' % (pred, y[rp[i]])
    displayData(X2, pred_str)
    plt.close()
 
# ЗАДАНИЕ №8
Error = numpy.where(pre != y.ravel())[0]
q = numpy.zeros((100,X.shape[1]))
for i in range(100):
    q[i] = X[Error[i]]
displayData(q)