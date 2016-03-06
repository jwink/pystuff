
from sklearn import datasets, svm, metrics

#import matplotlib.pyplot as plt


training_data = [[1], [5], [5], [5]];
training_values = [1, 3, 25, 3]

clf = svm.SVC(gamma=0.001, C=100)

X,y = training_data, training_values

clf.fit(X,y)

print(clf.predict([10]))


def lcs(S,T):
    m = len(S)
    n = len(T)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[i-c+1:i+1])

    return lcs_set

# test 1
ret = lcs('bacademy', 'abracadabra')
for s in ret:
    print s


ret = lcs('helloperson', 'hellozany')
x = ret.pop()
print x

print "helloperson".replace(x, "")
print "hellozany".replace(x, "")

