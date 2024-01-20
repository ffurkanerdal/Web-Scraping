from bs4 import BeautifulSoup
import requests


'https://example.com.tr/brand/url?tp=14&stoktakiler=1'


class CreateUrl:
    def __init__(self,url) -> None:
        self.url = url
        self.url_list = []

    def create_url(self,page_len):
        for num in range(int(page_len)):
            new_url = self.url + f'?tp={num}&stoktakiler=1'
            self.url_list.append(new_url)
        return self.url_list





class PullData:
    def __init__(self,url):
        self.url = url
        self.__get_soup = self.conn_url(self.url)

    def conn_url(self,url):
        headers = {
            'Write' : 'Headers'
            }
        cookies = {
            'Write' : 'Cookies'
        }
        response = requests.get(url,headers=headers,cookies=cookies)
        soup = BeautifulSoup(response.text,'html.parser')
        return soup

    def run(self):

        def pull_price():
            price_list = [i.text for i in self.__get_soup.find_all('div', class_='showcase-price')]
            return price_list

        def pull_brand():
            brand_list = [i.text for i in self.__get_soup.find_all('div', class_='showcase-brand')]
            return brand_list
        
        def pull_title():
            title_list = [i.text for i in self.__get_soup.find_all('div', class_='showcase-title')]
            return title_list

        def pull_image():
            image_list = [i['data-src'] for i in self.__get_soup.find_all('img',class_='lazyload')]
            return image_list

        return pull_price(), pull_brand(),pull_title(),pull_image()
    
