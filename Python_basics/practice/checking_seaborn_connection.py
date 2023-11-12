import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print ( sns.__version__ )

print (sns.get_dataset_names())

df = sns.load_dataset('titanic')
print ( df.head() )