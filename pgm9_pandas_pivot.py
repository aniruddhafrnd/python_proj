import pandas as pd
import xlrd
import numpy as np

df = pd.read_excel(r"C:\Aniruddha\Hadoop\python\test_prj\sales-funnel.xlsx")





df["new_status"] = df["Status"].astype("category")

df["new_status"].cat.set_categories(["won","pending","presented","declined"],inplace=True)
# print(type(df))
# print(type(df.dtypes))
#print (pd.pivot_table(df,index=["Manager","Rep"]))

#print(pd.pivot_table(df,index=["Name","Rep","Manager"],values=["Price"]))

#print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],columns=["Product"],aggfunc=[np.sum,len],fill_value=0))

#print(pd.pivot_table(df,index=["Manager","Rep","Product"],values=["Price","Quantity"],aggfunc=[np.sum],fill_value=0,margins=True))


#print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],columns=["Product"],aggfunc=[np.sum]))

#print(pd.pivot_table(df,index=["Manager","Rep"],values=["Price"],aggfunc=[np.sum]))

print (pd.pivot_table(df,index=["Manager","Status"],columns=["Product"],values=["Quantity","Price"],aggfunc={"Quantity":len,"Price":np.sum},fill_value=0))