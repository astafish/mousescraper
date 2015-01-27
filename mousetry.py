from bs4 import BeautifulSoup

import requests
import unicodecsv
import md5

f =open('listofeverything.csv', "wt")
writer = unicodecsv.writer(f)
writer.writerow( ('ID', 'source', 'title', 'link') )

# load the page with links

for n in range(1,209):
 
  r = requests.get("http://data.gov.uk/data/search?res_format=CSV&q=spending&page="+str(n)) 
  data = r.text

  soup = BeautifulSoup(data)

# get all the links from a page

  for link in soup.find_all('a', attrs={'class':'view-data-link'}):

# getting all the html from the links from a page

    q = requests.get("http://data.gov.uk"+link.get('href'))

    mouse1 = q.text

    soup1 = BeautifulSoup(mouse1)

# data link dogs, cat and bird is actually print. Ya know...

    dog= soup1.find_all('div', attrs={'class':'h1-subheading'})[0].find_all('a')[0].text.strip()

    bat= md5.new(dog).hexdigest()
    
    for datamenulink in soup1.find_all('div', attrs={'class':'dataset-resource'}):
        cat= datamenulink.find_all('div', attrs={'class':'dataset-resource-text'})[0].text.strip()
          
	bird= datamenulink.find_all('ul')[0].find_all('a')[1].get('href')      

        writer.writerow( (bat, dog, cat, bird) )

# hasing the name of the resource list (dog) 
