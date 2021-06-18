import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from main import action
from navec import Navec
import processing_dataset
from pydantic import BaseModel


# App creation
app = FastAPI()

path = 'navec_hudlit_v1_12B_500K_300d_100q.tar'
nana = Navec.load(path)
pdt = processing_dataset.processing_dataset()

class User(BaseModel):
    interests: str
    movies: str
    books: str
    music: str



@app.post('/companions')
def find_companions(user:User):
    return action(user.interests, nana, pdt)


if __name__ == '__main__':
    # Run server using given host and port
    uvicorn.run(app, host='127.0.0.1', port=80)
