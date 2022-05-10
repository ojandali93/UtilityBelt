from venv import create
import pandas as pd
import numpy as np

def createSubStringFromDataframe(dataset, argument, create_copy=True):
  if create_copy == True:
    dataset_copy = dataset 
    argument = dataset_copy[argument]
    subset = dataset_copy[argument]
    return subset