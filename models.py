from pydantic import BaseModel
from typing import List

#Aqui é a estrutura de dados para as partidas e estatísticas dos jogadores
class Partidas(BaseModel):
    match_id: str
    match_date: str
    match_name: str
    result: str
    score: str
    kills: int
    deaths: int
    assists: int
    rating: int
    mvps: str
    
class PlayerStats(BaseModel):
    steam_id: str
    player_name: str
    total_kills: int
    total_deaths: int
    total_assists: int