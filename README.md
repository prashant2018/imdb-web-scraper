## IMDB Web Scraper With MongoDb Connection with Python

#### About:
Scrape data from IMDB and store it to MongoDb.

Page to scrape: https://www.imdb.com/search/title/?release_date=2020

#### What the script does:
**1.** Extract following data:
* title
* rating
* actors
* summary
* img
* year
* certificate
* genre
* runtime
* director

**2.** Store it in local mongodb

### Detailed article
If you want to know more on how web scraping works, check out my article on [Medium](https://medium.com/@prashant2018/web-scraping-using-python-create-your-own-dataset-eb3f28129b6e)

#### Note:
This is only for learning web scraping as IMDB already provides data for educational use here: https://www.imdb.com/interfaces/

#### Setup:
```bash
# Install dependencies: 
pip install requirements.txt

# Run:
python Imdb_Movie_Info_Scraper.py
```

If you find this helpful and feel you want to contribute, feel free to do it at: [__Buy me a coffee! :coffee:__](https://www.buymeacoffee.com/prashant2018)

<a href="https://www.buymeacoffee.com/prashant2018" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
