from typing import Optional
from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = {
    "https://codepen.io/powerupta/pen/VwMKZXr?editors=0011"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"Greeting": "This is an RPS player"}


@app.get("/rps_play/")
def play_rps():
    api_choice = random.choice(["rock","paper","scissors"])
    return {"api_play": api_choice, "status": "success"}

@app.get("/rps_score/player/{player_choice}")
def score_rps(player_choice: str):
    api_choice = random.choice(["rock","paper","scissors"])
    score = {}
    score["result"] = scoregame(api_choice, player_choice)
    score["api"] = api_choice
    score["status"] = "success"
    return score

@app.get("/rps_score/player/{player_choice}/api/{api_choice}")
def score_rps(player_choice: str, api_choice: str):
    score = {}
    score["result"] = scoregame(api_choice, player_choice)
    score["api"] = api_choice
    score["status"] = "success"
    return score

def scoregame(api_choice, player_choice):
    if api_choice==player_choice:
        return "tie"
    elif api_choice=="rock" and player_choice=="paper":
        return "player"
    elif api_choice=="rock" and player_choice=="scissors":
        return "api"
    elif api_choice=="paper" and player_choice=="scissors":
        return "player"
    elif api_choice=="paper" and player_choice=="rock":
        return "api"
    elif api_choice=="scissors" and player_choice=="rock":
        return "player"
    elif api_choice=="scissors" and player_choice=="paper":
        return "api"
    else:
        return "unable to determine winner"