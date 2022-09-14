from API import API
from JSON import JSONManager
from urls import Directory


def get_match(matchid):
    url = API.match_by_matchid(matchid)
    match = API.get_json_result(url)
    JSONManager().save_json(match, f"{matchid}_summoner.json", Directory.EXAMPLES)
    return match

if __name__ == "__main__":
    # get_summoner("eC3QuRi6ZZ-WrAWRNfG3rjKWhPNZKdN7Y8JbWqZdtHY_lME4ydqSpsNyFw")
    # get_matchs("Miki")
    # KR_6117070430
    # KR_6084540009
    print(get_match("KR_6084540009"))
