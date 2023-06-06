from utils import configuration as config
from manifest import scrappingFunctions as progFunc
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from tqdm import tqdm  as tqdm


# HTTP Request for Father's Day Webpage of Amazon.com
webpage = requests.get(config.root_url, headers=config.HTTPS_HEADERS)

# Soup Object containing all data
soup = BeautifulSoup(webpage.content, "html.parser")

# Fetch links as List of Tag Objects
links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

# Store the links
links_list = []

# Loop for extracting links from Tag Objects
for link in tqdm(links) :
        links_list.append(link.get('href'))

d = {"title":[], "price":[], "rating":[], "reviews":[]}

# Loop for extracting product details from each link 
print("Performing the Web Scrapping, please wait a while.....")
for link in tqdm(links_list) :
    try :
        new_webpage = requests.get(
             "https://www.amazon.com" + link, 
              headers=config.HTTPS_HEADERS
            )
        
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # Function calls to display all necessary product information
        d['title'].append(progFunc.getTitleFunction(new_soup))
        d['price'].append(progFunc.getPriceFunction(new_soup))
        d['rating'].append(progFunc.getRatingFunction(new_soup))
        d['reviews'].append(progFunc.getReviewCountFunction(new_soup))
        
    except Exception as exp :
        print("HTTPS Exception occured.....")
        print("Ignoring and trying to continue....")
        continue
        
amazon_df = pd.DataFrame.from_dict(d)
amazon_df['title'].replace('', np.nan, inplace=True)
amazon_df = amazon_df.dropna(subset=['title'])
amazon_df.to_csv("amazon_data.csv", header=True, index=False)

