from requests import get

from key import public_key

class API:
    _BASE_URL = "https://kr.api.riotgames.com/lol"

    @staticmethod
    def league_url_by_league(league):
        return API._BASE_URL + f"/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={public_key}"

    @staticmethod
    def summoner_by_summonerID(summonerID):
        return API._BASE_URL + f"/summoner/v4/summoners/{summonerID}?api_key={public_key}"

    @staticmethod
    def get_json_result(url):
        return get(url).json()
