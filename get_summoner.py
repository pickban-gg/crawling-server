from API import API
from JSON import JSONManager
from urls import Directory


def get_summoner_by_puuid(puuid):
    summonerURL = API.summoner_by_puuid(summonerID=accountID)
    summoner = API.get_json_result(summonerURL)
    print(summoner)
    JSONManager().save_json(summoner, "_summoner.json", Directory.EXAMPLES)

def get_summoner_by_summonerName(summonerName):
    summonerURL = API.summoner_by_summonerName(summonerName)
    summoner = API.get_json_result(summonerURL)
    print(summoner)
    JSONManager().save_json(summoner, f"{summoner['name']}_summoner.json", Directory.EXAMPLES)
    return summoner

if __name__ == "__main__":
    # get_summoner("eC3QuRi6ZZ-WrAWRNfG3rjKWhPNZKdN7Y8JbWqZdtHY_lME4ydqSpsNyFw")
    get_summoner_by_summonerName("Miki")