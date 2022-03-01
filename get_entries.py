from API import API
from JSON import JSONManager
from urls import Directory


def get_entries():
    leagues = ["challengerleagues", "grandmasterleagues", "masterleagues"]
    for league in leagues:
        league_url = API.league_url_by_league(league)
        league_json_result = API.get_json_result(league_url)
        entries_json_result = league_json_result["entries"]
        league_file_name = league[:-1] + ".json"
        JSONManager().save_json(entries_json_result, league_file_name, directory_name=Directory.ENTRIES)


if __name__ == "__main__":
    get_entries()
