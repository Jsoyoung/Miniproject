import requests
import json
import pandas as pd

SERVICE_KEY = "6a4e556e6b6568663433776e41656b"

df=None
for i in range(301,375):
    URL=f'http://openapi.seoul.go.kr:8088/{SERVICE_KEY}/json/tbLnOpendataRtmsV/{1+(i-1)*1000}/{i*1000}/'
    print(URL)
    req= requests.get(URL)
    content=req.json()
    result=pd.DataFrame(content['tbLnOpendataRtmsV']['row'])
    df=pd.concat([df,result])
df=df.reset_index(drop=True)
df.to_csv('301-375.csv',index=False)

