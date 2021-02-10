def NegLogLike(Y_true, Fx):
    Y_prod = np.multiply(Y_true,Fx)
    Y_sum = np.sum(Y_prod, axis=-1)
    nll = -np.log(Y_sum+EPSILON)
    nll_mean = np.mean(nll)
    return nll_mean
