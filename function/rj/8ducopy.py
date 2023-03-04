# coding=utf-8
import pandas as pd
from pandas import DataFrame

def xinbie(val):
    if val is True:
        return "男"
    else:
        return "女"
data = {"ID":["01","02","03"],
      "name":["小龙","小强","小花"],
      "gender":["True","False","True"],
      "age":["14","13","15"],
      "height":["1.70","1.60","1.75"]
    }
frame=pd.DataFrame(data)
frame=frame.rename(columns={"ID":"学号","name":"名字","height":"身高"})
print(frame.to_csv())