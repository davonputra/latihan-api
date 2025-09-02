# command:
# install -> pip install"fastapi[standard]""

# import package
from fastapi import FastAPI, Header, HTTPException
import pandas as pd

# membuat object
app = FastAPI()

# api keys
password = "123456"

# execute
# command:
# fastapi dev nama file.py

# endpoint -> standard untuk, contoh: membuka halaman -> meminta data halaman utama
# 1. http function
# 2. url yang bisa diakses oleh client

@app.get("/")
def getMain():
    df = pd.read_csv('data.csv')



    return  {
        "message" : "Hello World",
        "hasil" : df.to_dict(orient="records")
    }

# setiap endpoint tidak boleh memiliki kombinasi http function dan url yang sama

# endpoint untuk mendapatkan data spesifik atau filter
# www.google.com/data/john cena -> response data john cena
# www.google.com/data/ucup -> response data ucup
# www.google.com/data/gilang -> response error (404 not found)
@app.get("/data{username}")
def getData(username: str):
    df = pd.read_csv('data.csv')

    # melakukan filter
    result = df.query(f"nama == '{username}'")

    return  {
        "message" : "Hello World",
        "hasil" : result.to_dict(orient="records")
    }

# endpoint untuk melakukan delete - protected
# jika tidak ada api key atau api key != password response error
# jika ada dan sesuai maka lanjut dulu -> success
@app.delete("/data/{username}")
def deleteData(username: str, api_key: str = Header(None)):
    # cek autentikasi
    if api_key == None or api_key != password:
        # response error
        raise HTTPException(status_code=401,detail="authentication gagal!")

    df = pd.read_csv('data.csv')

    # melakukan logic delete -> filter exclude
    result = df.query(f"nama != '{username}'")

    # export dataFrame ke csv/replace data baru
    result.to_csv('data.csv',index=False)

    return  {
        "message" : "Hello World",
        "hasil" : result.to_dict(orient="records")
    }