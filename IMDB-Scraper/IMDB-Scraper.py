# import the libraries
from bs4 import BeautifulSoup
import urllib.request as req
from tabulate import tabulate

# get the url of IMDB site

def url_link(url):
    response = req.urlopen(url)
    data = response.read()
    #print(data)
    soup = BeautifulSoup(data, "html.parser")
    return soup

# select the choice from the user

def select_choice():
    options = {
        1: ('Top Movies', 'top'),
        2: ('Most Popular Movies', 'moviesmeter'),
        3: ('Top English Movies', 'top-english movies'),
        4: ('Top TV Shows', 'toptv'),
        5: ('Most Popular TV Shows', 'tvmeter'),
        6: ('Low Rated Movies', 'bottom'),
        7: ('Top Box Office collection', 'boxoffice')
    }

    for i , option in enumerate(options, 1):
        print("{}) {}".format(i, options[option][0]))

    choice = int(input('Enter your choice: '))
    while(choice < 1 or choice > len(options)):
        print('Wrong option selected')
        choice = int(input('Enter your choice: '))
    return options[choice][1]

# Collect data from the url

def get_data(baseurl, option):
    complete_url = baseurl + option
    soup = url_link(complete_url)
    list1 = soup.find_all('span', {'class': 'media-body media-vertical-align'})
    print(soup)
    result = []
    count = 1

    for i in list1:
        try:
            name = i.find('h4').text.replace('\n', " ").lstrip("0123456789.- ")
        except:
            pass
        try:
            rating = i.find('p').text.strip()
        except:
            pass
        result.append([count, name, rating])
        count = count + 1
    print(tabulate(result, headers = ['Index', 'Name', 'Ratings'], tablefmt = 'grid'))

def main():
    base_url = "http://m.imdb.com/chart/"
    choice = select_choice()
    get_data(base_url, choice)

if __name__ == '__main__':
    main()