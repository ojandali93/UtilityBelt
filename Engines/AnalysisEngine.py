import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class DataAnalysisEngine(object):
  def __init__(self, dataset_url):
    self.dataset_url = dataset_url
    self.dataset = None
    self.no_null_dataset = None

  # Default functions that will read the dataset and store it
  def read_dataset(self):
    read_dataset = pd.read_csv(self.dataset_url)
    self.dataset = read_dataset
    self.dataset.head()

  # Print stats and summary about dataset
  def dataset_summary(self):
    print(self.dataset.describe())

  # Inspect some of the data from the dataset
  def dataset_quick_view(self):
    print(self.dataset.head(5))

  # Get Column Data Types
  def column_data_types(self):
    for col in self.dataset.columns:
      print(type(self.dataset[col]))

  # Validate null values 
  def check_and_remove_null(self):
    print(self.dataset.isna().sum())

  # Clean up dataset and remove null columns
  def clean_dataset_null_values(self):  
    print(self.dataset.columns)
    print(f'length of column list: {len(self.dataset.columns.tolist())}')
    total_record_count = len(self.dataset)
    self.dataset.isna().sum()
    for col in self.dataset.columns:
      total_column_count = self.dataset[col].isna().sum()
      percent_null_count = total_column_count / total_record_count
      if percent_null_count > .25:
        self.dataset.drop(columns=col)
    print(self.dataset.columns) 
    print(f'length of updated column list: {len(self.dataset.columns.tolist())}')

  # Drop all columns with with null data
  def drop_all_null_columns(self):
    for col in self.dataset.columns:
      null_value_count = self.dataset[col].isna().sum()
      if null_value_count > 0:
        self.dataset.drop(columns=col)
    return self.dataset.head(5)

  # Drop specific columns from dataset
  def drop_specific_columns(self, column_name):
    self.dataset.drop([column_name], axis = 1)
    print(self.dataset.columns) 
    return self.dataset.head(5)

  # Create subset of dataset
  def create_dataset_subset(self, argument):
    print(argument)
    self.dataset_copy = self.dataset[argument]
    print(f'The total number of records as a result of the subset: {len(self.dataset_copy)}')
    return self.dataset_copy

  # Get all unique values in a column
  def get_unique_column_value(self, column_name):
    # print(self.dataset[column_name].unique().tolist())
    return self.dataset[column_name].unique().tolist()