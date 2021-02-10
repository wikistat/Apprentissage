def softmax(X):
    expX = np.exp(X)
    sumExpX = np.sum(expX, axis=-1, keepdims=True)
    softmaxX = expX/sumExpX
    return softmaxX