#高华，20200117
import os
import  pandas as pd
files=os.listdir("data")#文件路径下的所有excel名列表
#取得表格表头
df=pd.read_excel("data/"+files[0])
df_final=pd.DataFrame(columns=df.columns)
#读取每一个文件，合并到dataframe中
for index,file in enumerate(files):
    df=pd.read_excel("data/"+file)
    df_final=df_final.append(df.drop(list(range(len(df)-3,len(df)))))
    print("文件{0}已合并".format(index))
df_final.to_excel("原始数据.xlsx")#输出文件输出到当前路径
