import numpy as np

def calculate(list):
    if len(list) == 9:
        dic = {}
        arr = np.array(list)
        re_arr = arr.reshape((3,3))
        dic['mean'] = [re_arr.mean(axis=0).tolist(), re_arr.mean(axis=1).tolist(), arr.mean().tolist()]
        dic['variance'] = [re_arr.var(axis=0).tolist(), re_arr.var(axis=1).tolist(), arr.var().tolist()]
        dic['standard deviation'] = [re_arr.std(axis=0).tolist(), re_arr.std(axis=1).tolist(), arr.std().tolist()]
        dic['max'] = [re_arr.max(axis=0).tolist(), re_arr.max(axis=1).tolist(), arr.max().tolist()]
        dic['min'] = [re_arr.min(axis=0).tolist(), re_arr.min(axis=1).tolist(), arr.min().tolist()]
        dic['sum'] = [re_arr.sum(axis=0).tolist(), re_arr.sum(axis=1).tolist(), arr.sum().tolist()]
        return dic   
    else:
        raise ValueError("List must contain nine numbers.")