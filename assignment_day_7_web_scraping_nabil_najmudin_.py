# -*- coding: utf-8 -*-
"""Assignment Day 7 - Web Scraping_Nabil Najmudin .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AiFYrpRqUoWHvGu0Y-LJI3C1kGGvRI6c

# BeautifulSoup
Deskripsi tugas:
- Tujuan: Membuat program untuk melakukan web scraping pada halaman web (https://quotes.toscrape.com) yang mengandung kutipan, penulis, dan tag-tag yang terkait dengan kutipan tersebut. Data hasil scraping akan disimpan dalam format CSV.
- Sumber Data: Halaman web yang berisi kutipan beserta informasi penulis dan tag-tag terkait.
- Tools yang Digunakan: Python, library BeautifulSoup untuk melakukan web scraping, library Pandas untuk manipulasi dan penyimpanan data dalam format CSV.
- Langkah-langkah:
  1. Menggunakan library requests, mengirim permintaan GET ke URL halaman web yang berisi kutipan.
  2. Menggunakan library BeautifulSoup, mengekstrak data kutipan, penulis, dan tag-tag terkait dari struktur HTML halaman web.
  3. Menyimpan data yang telah diekstrak ke dalam struktur data yang sesuai (misalnya, list atau DataFrame).
  4. Menggunakan library Pandas, menyimpan data ke dalam file CSV dengan menggunakan metode `to_csv()`.
- Output: File CSV yang berisi data kutipan, penulis, dan tag-tag terkait.
- Validasi: Melakukan pengecekan bahwa data yang telah diekstrak sesuai dengan struktur yang diharapkan dan bahwa file CSV telah berhasil dibuat dan berisi data yang benar.
- Kesimpulan: Setelah menjalankan program, data kutipan, penulis, dan tag-tag terkait telah berhasil diambil dari halaman web dan disimpan dalam file CSV, siap digunakan untuk analisis lebih lanjut atau tujuan lainnya.
"""

import requests

url = "https://quotes.toscrape.com"

page = requests.get(url)
page.headers

page.text

type(page.text)

type(page.content)

from bs4 import BeautifulSoup
# print(type(page.content))

soup = BeautifulSoup(page.content, 'html.parser')

type(soup)

quotes = soup.find_all("div", class_="quote") # find_all akan mengembalikan list (array)
type(quotes)

len(quotes)

quotes[0]

words = []
authors = []
tags_list = []

import pandas as pd

for quote in quotes:
    author = quote.find("small", class_="author").text.strip() # Mendapatkan nama penulis
    text = quote.find("span", class_="text").text.strip() # Mendapatkan teks kutipan

    # Mendapatkan semua tag
    tags = quote.find('div', class_='tags').find_all('a', class_='tag')
    tag_texts = [tag.text.strip() for tag in tags]

    # Menambahkan ke list
    authors.append(author)
    words.append(text)
    tags_list.append(tag_texts)

# Membuat DataFrame
df = pd.DataFrame({
    "authors": authors,
    "quotes": words,
    "tags": tags_list
})

print(df)

# Menyimpan DataFrame ke dalam file CSV
df.to_csv('quotes_data.csv', index=False)

print("Data berhasil disimpan dalam file 'quotes_data.csv'.")