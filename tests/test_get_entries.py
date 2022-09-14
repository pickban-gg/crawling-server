from unittest import TestCase

from key import public_key
from urls import API


class APITest(TestCase):
    def test_API_league_url_from_league(self):
        league = "challengerleagues"
        league_url = API.league_url_by_league(league)
        expected_league_url = f"https://kr.api.riotgames.com/lol/league/v4/{league}/by-queue/RANKED_SOLO_5x5?api_key={public_key}"
        self.assertEqual(expected_league_url, league_url)

    def test_API_summoner_by_accountID(self):
        accountID = "1"
        league_url = API.summoner_by_puuid(accountID)
        expected_league_url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-account/{accountID}?api_key={public_key}"
        self.assertEqual(expected_league_url, league_url)