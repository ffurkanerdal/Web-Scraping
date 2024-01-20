from bs4 import BeautifulSoup
import requests

class SiteMap:
    def __init__(self) -> None:
        self.url = 'https://example.com.tr/xml/example.xml?sr=45084ae5s'
        self.__xml_soup = self.conn_site()

    def conn_site(self):
        response=   requests.get(self.url)
        soup    =   BeautifulSoup(response.text,'xml')
        return soup
    
    def get_categories(self):
        category_list = [i.text for i in self.__xml_soup.find_all('loc')]
        return category_list

    def get_page_brand(self):
        page_brands     =   [i.text.split('/')[-1] for i in self.__xml_soup.find_all('loc')]
        return page_brands

    def get_page_len(self):
        pages = self.get_categories()
        page_len    =   []
        

        def conn_page(url):
            res     =   requests.get(url)
            soup    =   BeautifulSoup(res.text,"html.parser")
            divs    =   soup.find_all('div',class_='paginate-content')

            page_len.append('1' if len(divs) == 0 else str(divs[0].find_all('a')[-1].text))

        for url in pages:
            conn_page(url)
            print(f'{pages.index(url)+1}/{len(pages)}')
            
        return page_len
    
    def run(self):
        print('Controlling Categories')
        page_len    = self.get_page_len()
        category_list = self.get_categories()
        page_brands = self.get_page_brand()
        print('Controlling Page Len')

        dataset =   zip(category_list,page_len,page_brands)
        return list(dataset)

