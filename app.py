import uvicorn

from api_server import api_app

if __name__ == "__main__":
    uvicorn.run(api_app, port=4848, host='0.0.0.0')