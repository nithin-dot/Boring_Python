from ssl import CertificateError
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
  

# Downloading imdb top 250 movie's data
pages=12
paged=int(pages*100/2)
for page,minus in zip(range(1,paged,51),range(1,pages+1)):
    url = f'https://www.imdb.com/search/title/?genres=romance&sort=num_votes,desc&start={page-minus+1}&explore=title_type,genres&ref_=adv_nxt'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    movies =  soup.find("div", class_="lister-list")
    for div_list in movies.find_all("div", class_="lister-item mode-advanced"):
        # div_list=movies.find_all("div", class_="lister-item mode-advanced")
        movie_name=div_list.find("h3", class_="lister-item-header")
        ratings=div_list.find("div", class_="inline-block ratings-imdb-rating")
        Certificate=div_list.find("span", class_="lister-item-year text-muted unbold") 
        if(float(ratings.find("strong").text)>=7.5 and "–" not in Certificate.text):
            year_list=[x for x in Certificate.text if x.isdigit()]
            if(int("".join(year_list))>=2010):
                try:  
                        
                        print(f'Name :{movie_name.find("a").text}\nRating:{ratings.find("strong").text}\nYear Released:{int("".join(year_list))}')
                        print("https://www.imdb.com"+movie_name.find('a').get('href')+"\n")
                except:
                        print("e")





# crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
# ratings = [b.attrs.get('data-value')
#   for b in soup.select('td.posterColumn span[name=ir]')]




# # create a empty list for storing
# # movie information
# list = []

# # Iterating over movies to extract
# # each movie's details
# for index in range(0, len(movies)):
 
#  # Separating movie into: 'place',
#  # 'title', 'year'
#  movie_string = movies[index].get_text()
#  movie = (' '.join(movie_string.split()).replace('.', ''))
#  movie_title = movie[len(str(index))+1:-7]
#  year = re.search('\((.*?)\)', movie_string).group(1)
#  place = movie[:len(str(index))-(len(movie))]
#  data = {"place": place,
#    "movie_title": movie_title,
#    "rating": ratings[index],
#    "year": year,
#    "star_cast": crew[index],
#    }
#  list.append(data)

# # printing movie details with its rating.
# for movie in list:
#  print(movie['place'], '-', movie['movie_title'], '('+movie['year'] +
#   ') -', 'Starring:', movie['star_cast'], movie['rating'])


# ##.......##
# df = pd.DataFrame(list)
# print(df)
# df.to_csv('imdb_top_250_movies.csv',index=False)
