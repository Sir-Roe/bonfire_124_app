import requests
import pandas as pd

class Base:
    """
    Class handles all connection to the API object and returns a dataframe
    from it's initialization. 

    Class will have these methods:
    return_url: return API url that we are currently working with
    get_data: scrape the data from the API and create a dataframe for it
    """

    def __init__(self):

        self.api_url= "https://api.scryfall.com/bulk-data"
        self.get_data() 

    def return_url(self):
        return self.api_url
    
    def get_data(self):
        '''Scraping data from the API and creating a Dataframe from it'''
        response = requests.get(self.api_url)
        respone1=requests.get(response.json()['data'][0]['download_uri'])
        self.df = pd.DataFrame.from_dict(respone1.json())
        return self.df

if __name__ == '__main__':
    c= Base()
    c.df.to_csv('src/data/oracle_cards.csv',index=False)