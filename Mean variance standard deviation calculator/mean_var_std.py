import numpy as np

def calculate(list):
    if len(list)!=9:
        raise ValueError("List must contain nine numbers.")
    a=np.array(list).reshape(3,3)
    calculations={
'mean': [a.mean(axis=0).tolist(), a.mean(axis=1).tolist(), a.mean().tolist()],
'variance': [a.var(axis=0).tolist(), a.var(axis=1).tolist(), a.var().tolist()],
'standard deviation': [a.std(axis=0).tolist(), a.std(axis=1).tolist(), a.std().tolist()],
'max': [a.max(axis=0).tolist(), a.max(axis=1).tolist(), a.max().tolist()],
'min': [a.min(axis=0).tolist(), a.min(axis=1).tolist(), a.min().tolist()],
'sum': [a.sum(axis=0).tolist(), a.sum(axis=1).tolist(), a.sum().tolist()]
}
    return calculations