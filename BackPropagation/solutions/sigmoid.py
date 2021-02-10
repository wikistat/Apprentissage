def sigmoid(X):
    sigX = 1 / (1 + np.exp(-X))
    return sigX


def dsigmoid(X):
    sig=sigmoid(X)
    dsig = sig * (1 - sig)
    return dsig