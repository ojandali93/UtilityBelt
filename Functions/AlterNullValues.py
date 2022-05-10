import pandas as pd
import numpy as np

def alterNullValues(dataset, column_names=None, replacement=0):
  if column_names == None:
    dataset.fillna(replacement)
    return dataset
  if type(dataset) == list:
    columns = dataset.column().toList()
    for column in columns:
      dataset[column] = dataset[column].fillna(replacement)
    return dataset
  else:
    dataset[column] = dataset[column].fillna(replacement)
    return dataset