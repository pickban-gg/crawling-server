from API import API
from JSON import JSONManager
from get_summoner import get_summoner_by_summonerName
from get_matches import get_matches
from get_match import get_match
from urls import Directory

import datetime
ut = 1406204196


def get_matches_by_summonerName(summonerName):
    print(get_matches_by_summonerName, summonerName)
    summoner = get_summoner_by_summonerName(summonerName)
    puuid = summoner["puuid"]
    matches = get_matches(puuid)
    for matchid in matches:
        match = get_match(matchid)
        if match["info"]["queueId"] != 420:
            print(match["info"]["queueId"], matchid)
        # for participant in match["info"]["participants"]:
        #     if "Miki" == participant["summonerName"] and "Vayne" == participant["championName"]:
        #         # dt = datetime.datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
        #         print(match["info"]["gameCreation"], matchid)
        #         break

def get_queueIDs_by_summonerName(summonerName):
    print(get_matches_by_summonerName, summonerName)
    summoner = get_summoner_by_summonerName(summonerName)
    puuid = summoner["puuid"]
    matches = get_matches(puuid)
    for matchid in matches:
        match = get_match(matchid)
        for participant in match["info"]["participants"]:
            if "Miki" == participant["summonerName"] and "Vayne" == participant["championName"]:
                # dt = datetime.datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
                print(match["info"]["gameCreation"], matchid)
                break

def get_champion_name_of_currentGame(summonerName):
    print(get_matches_by_summonerName, summonerName)
    summoner = get_summoner_by_summonerName(summonerName)
    puuid = summoner["puuid"]
    matches = get_matches(puuid)
    count = 0
    for matchid in matches:
        if count > 30:
            return
        count += 1
        match = get_match(matchid)
        for participant in match["info"]["participants"]:
            if "Miki" == participant["summonerName"]:
                # dt = datetime.datetime.fromtimestamp().strftime('%Y-%m-%d %H:%M:%S')
                print(participant["championName"])
                break

def get_customMatch_by_summonerName(summonerName):
    print(get_matches_by_summonerName, summonerName)
    summoner = get_summoner_by_summonerName(summonerName)
    puuid = summoner["puuid"]
    matches = get_matches(puuid, queue = 0)
    # for matchid in matches:
    #     match = get_match(matchid)




if __name__ == "__main__":
    # get_summoner("eC3QuRi6ZZ-WrAWRNfG3rjKWhPNZKdN7Y8JbWqZdtHY_lME4ydqSpsNyFw")
    # get_matches_by_summonerName("Miki")
    # get_customMatch_by_summonerName("Miki")
    # get_champion_name_of_currentGame("Miki")
    get_matches_by_summonerName("Miki")