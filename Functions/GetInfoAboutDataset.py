import pandas as pd
import numpy as np

def GetInforAboutDataset(dataset):
  data_info = dataset.info()
  print(data_info)
  data_describe = dataset.describe()
  print(data_describe)
  data_null = dataset.isnull().sum()
  print(data_null)