#  Author: Darsh Jhunjhunwal
#  Date: 26-10-2023
# #Bio: I'm 7 years old. I like to do programming

import pandas as pd
from gettext import install

import pip

superstore_1 = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\Python\Python files\content\SampleSuperstore.csv")
superstore_2 = pd.read_csv(r"C:\Users\chand\OneDrive\Desktop\Python\Python files\content\inventory.csv")
# Preview first 5 rows of data set
superstore_1.head()

# Shape of data set
superstore_1.shape

superstore_1['Profit Margin %'] = (superstore_1.Profit / superstore_1.Sales) * 100
