import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.base_url = Config.BASE_URL
        self.timeout = Config.TIMEOUT
    def get(self,path,**kwargs):
        return requests.get(f"{self.base_url}{path}",timeout=self.timeout,**kwargs)
    def post(self,path,**kwargs):
        return requests.post(f"{self.base_url}{path}",timeout=self.timeout,**kwargs)

