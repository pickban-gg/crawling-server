from requests import get

from key import public_key

class API:
    _BASE_URL = "https://kr.api.riotgames.com/lol"
    _ASIA_URL = "https://asia.api.riotgames.com/lol"

    @staticmethod
    def league_url_by_league(league):
        return API._BASE_URL + f"/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={public_key}"

# /lol/summoner/v4/summoners/{summonerName}
    @staticmethod
    def summoner_by_summonerName(summonerName):
        return API._BASE_URL + f"/summoner/v4/summoners/by-name/{summonerName}?api_key={public_key}"

    @staticmethod
    def summoner_by_puuid(summonerID):
        return API._BASE_URL + f"/summoner/v4/summoners/{summonerID}?api_key={public_key}"

    @staticmethod
    def matches_by_puuid(puuid, queue = None):
        queueString = f"queue={queue}&"
        if queue == None:
            queueString = ""
        return API._ASIA_URL + f"/match/v5/matches/by-puuid/{puuid}/ids?{queueString}start=0&count=100&api_key={public_key}"

    @staticmethod
    def match_by_matchid(matchid):
        return API._ASIA_URL + f"/match/v5/matches/{matchid}?api_key={public_key}"


    @staticmethod
    def get_json_result(url):
        return get(url).json()
