# -*- coding: utf-8 -*-
"""Nasa_Scraper(1st method).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dbLomZLFbI66I_SBK5QJsGSgin3Y_HW3
"""

import requests
import csv
from bs4 import BeautifulSoup

class NASADataScraper:
    def __init__(self):
        self.base_url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"
        self.base_url = 'https://www.earthdata.nasa.gov'
        self.data = []

    def scrape_data(self):
        try:
            # Send an HTTP GET request to the data URL
            response = requests.get(self.base_url)
            response.raise_for_status()

            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Find the relevant data on the page (modify this as per your requirements)
            data_elements = soup.find_all("div", class_="data-element")

            for element in data_elements:
                # Extract the data you need from each element (modify this as per your requirements)
                title = element.find("h3").text
                description = element.find("p").text
                link = element.find("a")["href"]

                # Append the extracted data to the list
                self.data.append({
                    "Title": title,
                    "Description": description,
                    "Link": link,
                })

        except requests.exceptions.RequestException as e:
            print("Error:", e)

    def save_to_csv(self, output_file):
        try:
            with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
                fieldnames = ["Title", "Description", "Link"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Write header row
                writer.writeheader()

                # Write data rows
                for item in self.data:
                    writer.writerow(item)

            print(f"Data saved to {output_file}")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    scraper = NASADataScraper()
    scraper.scrape_data()
    scraper.save_to_csv("nasa_data.csv")

