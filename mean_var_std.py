import numpy as np

def calculate(list):
    # check count of list elements
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    # convert list into 3*3 numpy array
    list_into_array = np.array(list)
    reshapedArray = list_into_array.reshape(3,3)
    
    
    mean_list = [np.mean(reshapedArray, axis=0).tolist(), np.mean(reshapedArray, axis=1).tolist(), np.mean(reshapedArray).tolist()]
    variance_list = [np.var(reshapedArray, axis=0).tolist(), np.var(reshapedArray, axis=1).tolist(), np.var(reshapedArray).tolist()]
    std_list = [np.std(reshapedArray, axis=0).tolist(), np.std(reshapedArray, axis=1).tolist(), np.std(reshapedArray).tolist()]
    max_list = [np.max(reshapedArray, axis=0).tolist(), np.max(reshapedArray, axis=1).tolist(), np.max(reshapedArray).tolist()]
    min_list = [np.min(reshapedArray, axis=0).tolist(), np.min(reshapedArray, axis=1).tolist(), np.min(reshapedArray).tolist()]
    sum_list = [np.sum(reshapedArray, axis=0).tolist(), np.sum(reshapedArray, axis=1).tolist(), np.sum(reshapedArray).tolist()]
        
    calculations= {}
    calculations['mean'] = mean_list
    calculations['variance'] = variance_list
    calculations['standard deviation'] = std_list
    calculations['max'] = max_list
    calculations['min'] = min_list
    calculations['sum'] = sum_list

    return calculations