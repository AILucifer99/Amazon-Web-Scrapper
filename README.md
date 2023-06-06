# Amazon-Web-Scrapper
An implementation of a web scrapping application using Python's Requests and BeautifulSoup Libraries. 
Code writen for `https://amazon.com/` accordingly.

## Usage of the Repository
1.   First, Clone the repository using the command `git clone https://github.com/AILucifer99/Amazon-Web-Scrapper.git`
2.   Second, Change the working directory using the command `cd Amazon-Web-Scrapper`
3.   Third, Run the command `pip install -r requirements.txt`
4.   Finally, In the command prompt type `python main.py` for performing the Web Scrapping. 

## Configuration
Just change the `root_url` variable inside the `utils` module
Example of root_urls are :- 
1.   For Headphones :- `root_url = https://www.amazon.com/s?k=headphones&crid=1IYRGVSJT78SK&sprefix=headphones%2Caps%2C339&ref=nb_sb_noss_2`
2.   For Apple Iphones :- `root_url = https://www.amazon.com/s?k=apple+iphone&sprefix=%2Caps%2C286&ref=nb_sb_ss_recent_5_0_recent`
3.   For Toys :- `root_url = https://www.amazon.com/s?k=toys&crid=2H3NANKXQHUQL&sprefix=toys%2Caps%2C291&ref=nb_sb_noss_1`
4.   For stuffed animals :- `root_url = https://www.amazon.com/s?k=stuffed+animals&crid=2IFQEQVV74KK6&sprefix=Stuffed%2Caps%2C284&ref=nb_sb_ss_ts-doa-p_2_7`
