import pandas as pd

url = 'https://docs.google.com/document/d/e/2PACX-1vSCJGXDu491Y3rRgJPVhtdsY5ivkbQ5FJMDvPyanh2F7HNk2cea9AZIHa1j-RShETAsCxKqqbZ_Vz7J/pub'
df = pd.read_html(url, encoding = 'utf-8')
print(df[0])