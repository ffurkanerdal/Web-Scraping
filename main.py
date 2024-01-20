from sitemap import SiteMap as urlList
from pull import CreateUrl,PullData
from writeDB import Data,session

class Main:

    def __nestedUrls(self):
        nested_urls = []    
        
        for url in urlList().run():
            nested_urls.append(CreateUrl(url[0]).create_url(url[1]))
        
        return nested_urls
    
    def pullData(self):
        for urls in self.__nestedUrls():
            for url in urls:
                dataset = PullData(url).run() # 0 => Price 1 => Brand 2=> Name 3=> Image
                self.writeDB(dataset)

    def writeDB(self,dataset):
        for price,brand,name,image in zip(dataset[0],dataset[1],dataset[2],dataset[3]):
            data = Data(name=name,image=image,brand=brand,price=price)
            session.add(data)
        session.commit()
    
    
Main().pullData()
                
