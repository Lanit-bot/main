import fasttext
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from main import action

# App creation
app = FastAPI()


@app.post('/companions')
def find_companions(user):
    return action(user)


if __name__ == '__main__':
    # Run server using given host and port
    uvicorn.run(app, host='127.0.0.1', port=80)
