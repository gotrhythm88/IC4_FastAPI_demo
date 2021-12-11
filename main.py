from fastapi import FastAPI
import random
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://codepen.io/",
    "https://cdpn.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"Greetings": "This is an RPS player"}


@app.get("/rps_score/playermove/{player_choice}")
def score_rps(player_choice: str):
    api_choice = random.choice(["rock","paper","scissors"])
    score = {}
    score["result"] = scoregame(api_choice, player_choice)
    score["api"] = api_choice
    score["status"] = "success"
    return score

def scoregame(api_choice, player_choice):
    if api_choice==player_choice:
        return "It's a TIE"
    elif api_choice=="rock" and player_choice=="paper":
        return "YOU WIN!!"
    elif api_choice=="rock" and player_choice=="scissors":
        return "The API defeated you"
    elif api_choice=="paper" and player_choice=="scissors":
        return "YOU WIN!!"
    elif api_choice=="paper" and player_choice=="rock":
        return "The API defeated you"
    elif api_choice=="scissors" and player_choice=="rock":
        return "YOU WIN!!"
    elif api_choice=="scissors" and player_choice=="paper":
        return "The API defeated you"
    else:
        return "unable to determine winner"