from API import API
from JSON import JSONManager
from urls import Directory

def get_matches(puuid, queue = None):
    url = API.matches_by_puuid(puuid, queue)
    matches = API.get_json_result(url)
    JSONManager().save_json(matches, f"{puuid}'s matches.json", Directory.EXAMPLES)
    print(matches, url)
    return matches

if __name__ == "__main__":
    # get_summoner("eC3QuRi6ZZ-WrAWRNfG3rjKWhPNZKdN7Y8JbWqZdtHY_lME4ydqSpsNyFw")
    get_matchs("Miki")