import numpy as np

def calculate(list_num):
    if(len(list_num) != 9 ):
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list_num)
    new_arr = arr.reshape((3,3))
    


    final_dict = {
        'mean' : [list(new_arr.mean(axis = 0)), list(new_arr.mean(axis = 1)), arr.mean() ],
        'variance': [list(new_arr.var(axis = 0)), list(new_arr.var(axis = 1)), arr.var()],
        'standard deviation': [list(new_arr.std(axis = 0)), list(new_arr.std(axis = 1)), arr.std()],
        'max': [list(new_arr.max(axis = 0)), list(new_arr.max(axis = 1)), arr.max()],
        'min': [list(new_arr.min(axis = 0)), list(new_arr.min(axis = 1)), arr.min()],
        'sum': [list(new_arr.sum(axis = 0)), list(new_arr.sum(axis = 1)), arr.sum()]
    }


    return final_dict