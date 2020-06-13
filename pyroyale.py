import sys
import requests

class PyRoyale:
    def __init__(self, api_key):
        """ Add api key to class """
        self.api_key = api_key
        self.headers = {"Accept": "application/json",
               "authorization": "Bearer " + api_key}


    # --- Retrieve all clan JSON info ---
    
    # TODO: Add capability for /clan searches

    def get_clan_info(self, clan_tag):
        """ /clans endpoint """
        url = "https://api.clashroyale.com/v1/clans/%23" + clan_tag
        self.clan_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data

    def get_clan_member_info(self, clan_tag):
        """ /clans/{clantag}/members endpoint """
        url = "https://api.clashroyale.com/v1/clans/%23" + clan_tag + '/members'
        self.clan_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    
    def get_clan_warlog(self, clan_tag):
        """ /clans/{clantag}/warlog endpoint """
        url = "https://api.clashroyale.com/v1/clans/%23" + clan_tag + '/warlog'
        self.clan_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data

    def get_clan_currentwar(self, clan_tag):
        """ /clans/{clantag}/currentwar endpoint """
        url = "https://api.clashroyale.com/v1/clans/%23" + clan_tag + '/currentwar'
        self.clan_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    # --- End of Clan JSON info retrieval ---

    # --- Retrieve all player info ---
    def get_player_info(self,tag):
        """ api call used for info of a single player """ 
        url = "https://api.clashroyale.com/v1/players/%23" + tag
        self.player_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    

        #keys = ['tag', 'name', 'expLevel', 'trophies', 'wins', 'losses', 'bestTrophies']
        #self.player_info = [data[key] for key in keys] # Convert JSON to list

    def get_player_upcomingchests(self,tag):
        """ Call used to view upcoming chests """
        url = "https://api.clashroyale.com/v1/players/%23" + tag + '/upcomingchests'
        self.player_upcomingchests = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    
    def get_player_battelog(self,tag):
        url = "https://api.clashroyale.com/v1/players/%23" + tag + '/battlelog'
        self.player_battlelog = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    # --- End of player info section

    # --- Start of Clash Royale card info retrieval ---
    def get_card_info(self):
        """ /clans/{clantag}/currentwar endpoint """
        url = "https://api.clashroyale.com/v1/cards"
        self.card_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
    # --- End of card info retrieval ---

    # -- Start of Tournament / Global Tournament info ---
    
    # TODO: Create custom searching for tournaments

    def get_tournament_info(self, tournament_tag):
        """ /tournaments/{tournamentstag} endpoint """
        url = "https://api.clashroyale.com/v1/tournaments" + tournament_tag
        self.tournament_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data

    def get_global_tournaments(self):
        """ /globaltournaments endpoint """
        url = "https://api.clashroyale.com/v1/globaltournaments"
        self.global_tournament_info = requests.request("GET", url, headers=self.headers).json() # Retrieve JSON data
        
    # --- End of Tournament / Global Tournament info ---
