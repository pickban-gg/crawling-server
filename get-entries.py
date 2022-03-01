from requests import get
import json
import os
from key import public_key

JSON_RESULTS_URL = "./json-results/leagues"
def save_json(json_data, file_name):
    os.makedirs(JSON_RESULTS_URL, exist_ok = True)
    with open(f"{JSON_RESULTS_URL}/{file_name}", "w") as json_file:
        json.dump(json_data, json_file)

def get_json_result(url):
    return get(url).json()

def get_url_from_league(league):
    return f"https://kr.api.riotgames.com/lol/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={public_key}" 

def get_entries():
    leagues = ["challengerleagues", "grandmasterleagues", "masterleagues"]
    for league in leagues:
        league_url = get_url_from_league(league)
        league_json_result = get_json_result(league_url)
        entries_json_result = league_json_result["entries"]
        league_file_name = league[:-1] + ".json"
        save_json(entries_json_result, league_file_name)

if __name__ == "__main__":
    get_entries()