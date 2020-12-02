import numpy 
import scipy.io
from displayData import displayData
from predict import predict
import matplotlib.pyplot as plt

# ЗАДАНИЕ №1
test_set = scipy.io.loadmat('test_set.mat')
weights = scipy.io.loadmat('weights.mat')

# ЗАДАНИЕ №2
X_test = test_set['X']
y_test = numpy.int64(test_set['y']).ravel()
Theta1 = weights['Theta1']
Theta2 = weights['Theta2']
m = X_test.shape[0]


# ЗАДАНИЕ №3
Index = numpy.random.permutation(m)
k = X_test[Index[:100]]
displayData(k)

# ЗАДАНИЕ №6
pre = predict(Theta1, Theta2, X_test)
result = numpy.mean(numpy.double(pre == y_test))
print(result)

# ЗАДАНИЕ №7
rp = numpy.random.permutation(m)
plt.figure()
for i in range(5):
    X2 = X_test[rp[i],:]
    X2 = numpy.matrix(X_test[rp[i]])
    pred = predict(Theta1, Theta2, X2.getA())
    pred = numpy.squeeze(pred)
    pred_str = 'Neural Network Prediction: %d (digit %d)' % (pred, y_test[rp[i]])
    displayData(X2, pred_str)
    plt.close()
 
# ЗАДАНИЕ №8
Error = numpy.where(pre != y_test)[0]
q = X_test[Error[:100]]    
displayData(q)
