import scipy.io
import pandas as pd
from scipy.io import loadmat

data=loadmat('file2.mat')
# Get a list of the variable names in the .mat file
var_names = list(data.keys())

# Print the list of variable names
print(var_names)

# Load a variable that you know is present in the .mat file
X = data['output_a']

df=pd.DataFrame(X)
df.to_csv("file2.csv")
