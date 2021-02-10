def one_hot(n_classes,y):
    ohy = np.eye(n_classes)[y]
    return ohy