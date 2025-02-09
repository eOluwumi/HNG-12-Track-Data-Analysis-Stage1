import pandas as pd

# Load the dataset
file_path = r"C:\Users\DELL\OkikiJESUS VsCode\Stage1- HNG12/productdata.xlsx - Sheet1.csv"

df = pd.read_csv(file_path)

# Display basic info about the dataset
df.info()
# df.head()
