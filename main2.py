from typing import Optional

from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/rps_play/")
def play_rps():
    api_choice = random.choice(["rock","paper","scissors"])
    return {"play": api_choice}

@app.get("/rps_score/player/{player_choice}")
def score_rps(player_choice: str):
    api_choice = random.choice(["rock","paper","scissors"])
    scoregame(api_choice, player_choice)

@app.get("/rps_score/player/{player_choice}/api/{api_choice}")
def score_rps(player_choice: str, api_choice: str):
    scoregame(api_choice, player_choice)

def scoregame(api_choice, player_choice):
    if api_choice==player_choice:
        return {"result": "tie"}
    elif api_choice=="rock" and player_choice=="paper":
        return {"result": "player"}
    elif api_choice=="rock" and player_choice=="scissors":
        return {"result": "api"}
    elif api_choice=="paper" and player_choice=="scissors":
        return {"result": "player"}
    elif api_choice=="paper" and player_choice=="rock":
        return {"result": "api"}
    elif api_choice=="scissors" and player_choice=="rock":
        return {"result": "player"}
    elif api_choice=="scissors" and player_choice=="paper":
        return {"result": "api"}
    else:
        return {"result": "unable to determine winner"}