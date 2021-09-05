import os
#import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from lib_one import main

stage = os.environ.get('STAGE', None)
openapi_prefix = f"/{stage}" if stage else "/"

app = FastAPI(title="MyAwesomeApp", openapi_prefix=openapi_prefix) # Here is the magic
@app.get("/hello")
def hello_world():
    res=main.getResponse()
    return {"message": "Hello World" + res}

handler = Mangum(app)

#if __name__ == "__main__":
 #   uvicorn.run(app, host="0.0.0.0", port=8000)