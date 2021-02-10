import pandas as pd
import numpy as np

def my_read_csv(filename):
    return pd.read_csv(filename, delim_whitespace=True, header=None)

def load_signal(directory, dataset, signal):
    filename = directory+"/"+dataset+'/Inertial Signals/'+signal+'_'+dataset+'.txt'
    x = my_read_csv(filename).values
    return x 

def load_signals(directory, dataset, signals):
    signals_data = []
    for signal in signals:
        signals_data.append(load_signal(directory, dataset, signal)) 
    X = np.transpose(signals_data, (1, 2, 0))
        
    return X 

def load_y(directory,dataset = "train"):
    filename = directory+"/"+dataset+'/y_'+dataset+'.txt'
    y = my_read_csv(filename)[0]
    Y = y.values
    return Y