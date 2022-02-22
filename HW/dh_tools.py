import pandas as pd

a = pd.read_csv('tools_dh_proceedings.csv').sort_values('2019', ascending= False)
