from API import API
from JSON import JSONManager
from urls import Directory


def get_summoner():
    accountID = "eC3QuRi6ZZ-WrAWRNfG3rjKWhPNZKdN7Y8JbWqZdtHY_lME4ydqSpsNyFw"
    summonerURL = API.summoner_by_summonerID(summonerID=accountID)
    summoner = API.get_json_result(summonerURL)
    print(summoner)
    JSONManager().save_json(summoner, "summoner.json", Directory.EXAMPLES)

if __name__ == "__main__":
    get_summoner()