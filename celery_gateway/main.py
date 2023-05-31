import uvicorn
from src.app import create_app


app, server_config = create_app()


if __name__ =="__main__":
    uvicorn.run(app, **server_config)