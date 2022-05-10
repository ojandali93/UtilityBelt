import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class DataVisualEngine(object):
  def __init__(self, dataset_url):
    self.dataset_url = dataset_url
    self.dataset = None
    self.no_null_dataset = None
    self.analysis_engine = None

    def read_dataset(self):
      read_dataset = pd.read_csv(self.dataset_url)
      self.dataset = read_dataset
      self.dataset.head()

    def dataset_describe(self):
      return self.dataset.describe

    def create_instance_of_analysis_engine(self):
      self.analysis_engine = DataAnalysisEngine(self.dataset_url)
      self.analysis_engine.read_dataset()
      self.analysis_engine.dataset_summary()


    def generate_bar_chart(self, x_axis, y_axis, x_label, y_label, title, color):
      fig = plt.figure(figsize=(20,8))
      ax = fig.add_axes([0,0,1,1])
      x_axis = self.dataset[self.dataset[x_axis]]
      y_axis = self.dataset[self.dataset[y_axis]]
      ax.set_xlabel(x_label)
      ax.set_ylabel(y_label)
      ax.set_title(title)
      ax.bar(x_axis,y_axis, color=color)
      plt.show()

    def generate_compared_bar_chart(self, subset, labels_subset, x_sxis, y_axis, y_label, x_label, title, color1, color2):
      labels = self.dataset[subset].unique()
      width = 0.4

      x = np.arange(len(labels))
      fig = plt.figure(figsize=(22,8))
      ax = fig.add_axes([0,0,1,1])

      ax.set_ylabel(y_label)
      ax.set_xlabel(x_label)
      ax.set_title(title)
      ax.set_xticks(x, labels)

      rect_fatal = ax.bar(x - width/2, x_axis, .4, label=x_label, color=color1)
      rect_non_fatal = ax.bar(x + width/2, y_axis, .4, label=y_label, color=color2)

      ax.bar_label(rect_fatal, padding=3)
      ax.bar_label(rect_non_fatal, padding=3)
      ax.legend()

      plt.show()

    def generate_scatter_plot(self, x_axis, y_axis, x_label, y_label, title, color):
      fig=plt.figure(figsize=(20,8))
      ax=fig.add_axes([0,0,1,1])
      x_axis = self.dataset[self.dataset[x_axis]]
      y_axis = self.dataset[self.dataset[y_axis]]
      ax.scatter(x_axis, y_axis, color=color)
      ax.set_xlabel(x_label)
      ax.set_ylabel(y_label)
      ax.set_title(title)
      plt.show()

    def generate_compared_scatter_plot(self, compared, x_axis, y_axis, x_label, y_label, title, color1, color2):
      scatter_compare = self.dataset[compared].unique() 
      scatter_x = self.dataset[self.dataset[x_axis]]
      scatter_y = self.dataset[self.dataset[x_axis]]

      fig=plt.figure(figsize=(20,8))
      ax=fig.add_axes([0,0,1,1])
      ax.scatter(scatter_compare, scatter_x, color=color1, label=x_label)
      ax.scatter(scatter_compare, scatter_y, color=color2, label=y_label)
      ax.set_xlabel(x_label)
      ax.set_ylabel(y_label)
      ax.set_title(title)
      ax.legend()
      plt.show()
