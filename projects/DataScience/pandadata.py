import pandas as pd
data={'Name':['santosh','sonu','sandeep','ajay'],
      'Age':['25','24','28','29'],
      'Address':['malad','kandavali','goregaon','khar'],
      'Qualification':['MCA','10','BCA','BSc']}
df=pd.DataFrame(data)
df.to_csv("santosh.csv",index=False)

df1=pd.read_csv("santosh.csv")
print(df)
