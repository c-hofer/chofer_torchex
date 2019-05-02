import torch 
import numpy as np


def ds_random_subset(dataset, percentage=None, absolute_size=None, replace=False):
    assert isinstance(dataset, torch.utils.data.dataset.Dataset)
    assert percentage is not None or absolute_size is not None
    assert not (percentage is None and absolute_size is None)
    if percentage is not None: assert 0 < percentage and percentage < 1, "percentage assumed to be > 0 and < 1"
    if absolute_size is not None: assert absolute_size <= len(dataset)
    
    n_samples =  int(percentage*len(dataset)) if percentage is not None else absolute_size
    indices = np.random.choice(list(range(len(dataset))), 
                            n_samples, 
                            replace=replace)
    
    indices = [int(i) for i in indices]
    
    return torch.utils.data.dataset.Subset(dataset, indices)

def ds_label_filter(dataset, labels):
    assert isinstance(labels, (tuple, list)), "labels is expected to be list or tuple."
    assert len(set(labels)) == len(labels), "labels is expected to have unique elements."
    assert hasattr(dataset, 'targets'), "dataset is expected to have 'targets' attribute"
    assert set(labels) <= set(dataset.targets), "labels is expected to contain only valid labels of dataset"
    
    indices = [i for i in range(len(dataset)) if dataset.targets[i] in labels]
    
    return torch.utils.data.dataset.Subset(dataset, indices)