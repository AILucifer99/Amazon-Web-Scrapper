from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from tqdm import tqdm as tqdm


# Function to extract Product Title
def getTitleFunction(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def getPriceFunction(soup):

    try:
        price = soup.find("span", attrs={"class": "a-price aok-align-center"}).find(
                "span", attrs={"class": "a-offscreen"}
            ).text.strip()
        
    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={"class": "a-offscreen"}).string.strip()

        except:
            price = ""

    return price


# Function to extract Product Rating
def getRatingFunction(soup):

    try:
        rating = soup.find("i", attrs={"class" : "a-icon a-icon-star a-star-4 cm-cr-review-stars-spacing-big"}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""	

    return rating


# Function to extract Number of User Reviews
def getReviewCountFunction(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count


# Function to extract Availability Status
def getAvailabilityFunction(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"	

    return available