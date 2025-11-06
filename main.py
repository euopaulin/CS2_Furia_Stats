from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Partidas, PlayerStats

#Instancia da aplicação FastAPI

MOCK_STEAM_ID = "76561198169203075"

MOCK_STATS = PlayerStats(
    steam_id=MOCK_STEAM_ID,
    player_name="Baulixn",
    total_kills=100,
    total_deaths=50,
    total_assists=25
)