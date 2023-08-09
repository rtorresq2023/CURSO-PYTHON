# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 08:01:55 2023

@author: Juan Carlos
"""

import requests
from bs4 import BeautifulSoup

def get_books_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        book_data = []
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip('£')
            book_data.append((title, float(price)))

        return book_data
    else:
        print(f"Error {response.status_code}: Unable to fetch the data.")
        return None


url = "http://books.toscrape.com/"
book_data = get_books_info(url)

if book_data:
    print("Book Title\t\tPrice (GBP)")
    print("-----------------------------------")
    for title, price in book_data:
        print(f"{title}\t\t{price}")
else:
    print("No data found. Please check the URL or try again later.")
