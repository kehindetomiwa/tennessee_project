import pandas as pd

def get_X(x_list):
    X = []
    x_mean = np.mean(x_list,axis=0)
    X.append(x_mean)
    x_list_move = move(x_list, 1)
    for x0, x1 in zip(x_list, x_list_move):
        X.append((x0-x1))
    X += x_list
    return X
