import pandas as pd
import numpy as np

import matplotlib.image as mpimg

from scipy.io import wavfile

def readInDatabase(file_path, type):
  if type == 'tabular':
    dataset = pd.read_csv(file_path)
    return dataset
  if type == 'image':
    img = mpimg.imread(file_path)
    return img 
  if type == 'audio':
    audio = wavfile.read(file_path)
    return audio