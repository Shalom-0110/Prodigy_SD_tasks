import requests
import csv
from bs4 import BeautifulSoup

# URL of the e-commerce API
url = "https://fakestoreapi.com/products/"

# Fetch the data from the API
response = requests.get(url)
products = response.json()

# Use BeautifulSoup to parse the JSON data as a string
soup = BeautifulSoup(str(products), 'html.parser')

# Define the CSV file name
csv_file = "products.csv"

# Open the CSV file for writing
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write the product data with clear structure
    for product in products:
        title = product.get("title")
        price = product.get("price")
        rating = product.get("rating", {}).get("rate")  # Handle nested rating dictionary
        
        writer.writerow([f"title: {title}"])
        writer.writerow([f"price: {price}"])
        writer.writerow([f"rating: {rating}"])
        writer.writerow([])  # Add an empty row for separation

print(f"Data has been written to {csv_file}")

