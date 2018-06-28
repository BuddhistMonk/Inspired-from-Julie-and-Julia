from sklearn.datasets import load_iris
import numpy as np

data = load_iris()

features = data['data']
feature_name = data['feature_names']
target = data['target']

# Creating multiple plots

import matplotlib.pyplot as plt

plt.figure()
fig, ax = plt.subplots(3,2,figsize=(17,9))
plt.show()