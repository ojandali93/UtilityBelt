import pandas as pd
import numpy as np

def eliminateNullValues(dataset, column_names=None, threshold=0):
  if columnName == None:
    columns = dataset.columns().toList()
    for column in columns:
      null_value_count = dataset[column].isnull().sum()
      total_value_count = len(dataset)
      percent_null = null_value_count / total_value_count
      if percent_null > threshold:
        dataset[column].dropna()
    return dataset
  elif type(column_names) == array:
    for column in column_names:
      null_value_count = dataset[column].isnull().sum()
      total_value_count = len(dataset)
      percent_null = null_value_count / total_value_count
      if percent_null > threshold:
        dataset[column].dropna()
    return dataset
  else:
    dataset[column_names].dropna()
    return dataset