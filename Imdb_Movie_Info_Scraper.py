import requests
import bs4
from pymongo import MongoClient

class MovieFetcher():
    
    def __init__(self,year):
        self.client = MongoClient('127.0.0.1',27017)
        self.db = self.client.movieDb
        self.collection = self.db["movies"+str(year)]
        
        
    def fetchInfo(self,url):
        return (requests.get(url)).text
    
    def scrapInfo(self, text):
        rsoup = bs4.BeautifulSoup(responseText,features="html.parser")
        movie_class = ".lister-item-content"
        image_class = ".lister-item-image"
        full_class = ".lister-item.mode-advanced"
        movie_list = rsoup.select(full_class)
        movie_data = []
        for full_content in movie_list:
            
            movie = full_content.select(movie_class)[0]
            imageData = full_content.select(image_class)[0]
            data = {}
            try:
                data['img'] = imageData.select("img")[0].get("loadlate")
            except:
                data['img'] = ''
            
            try:
                data['title'] = movie.find('a').text
            except:
                data['title'] = ''
            
            try:
                data['year'] = movie.select(".lister-item-year")[0].text
            except:
                data['year'] = ''
                
            try:
                data['certificate'] = movie.select('.certificate')[0].text
            except:
                data['certificate'] = ''
            try:
                data['runtime'] = movie.select('.runtime')[0].text
            except:
                data['runtime'] = ''
            try:
                data['genre'] = movie.select('.genre')[0].text.replace('\n','').strip().split(',')
            except:
                data['genre'] = ''
            
            try:
                data['rating'] = movie.select('.ratings-imdb-rating')[0].get("data-value")
            except:
                data['rating'] = ''
                
            try:
                data['summary'] = movie.select('p')[1].text.replace('\n','').strip()
            except:
                data['summary'] = ''
            
            try:
                dkey = movie.select('p')[2].text.replace('\n','').split('|')[0].strip().split(':')[0]
                dval = movie.select('p')[2].text.replace('\n','').split('|')[0].strip().split(':')[1].replace(', ',',').split(',')
                data[dkey] = dval
            except Exception as e:
                pass
                
            try:
                dkey = movie.select('p')[2].text.replace('\n','').split('|')[1].strip().split(':')[0]
                dval = movie.select('p')[2].text.replace('\n','').split('|')[1].strip().split(':')[1].replace(', ',',').split(',')
                data[dkey] = dval
            except Exception as e:
                pass
                
            movie_data.append(data)
            
        return movie_data
    
    def saveToDb(self,data):
        result = self.collection.insert_many(data,ordered=False)
        return result.inserted_ids
        
        
if __name__=='__main__':
    year = 2020
    start = 1
    movieFetcher = MovieFetcher(year)    
    responseText = movieFetcher.fetchInfo(f"https://www.imdb.com/search/title/?release_date={year}&start={start}")
    movie_data = movieFetcher.scrapInfo(responseText)
    res = movieFetcher.saveToDb(movie_data)
    print("Completed!")