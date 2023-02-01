import requests
import re

# Set the user agent to the latest Mozilla Firefox
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

# Request the XML from the URL
response = requests.get("https://www.example.com/productsxml/", headers=headers)

# Get the status code
status_code = response.status_code

# Color the status code message based on the value
if status_code >= 200 and status_code < 300:
    print("\033[32mStatus code:", status_code, "\033[0m")
elif status_code >= 300 and status_code < 400:
    print("\033[33mStatus code:", status_code, "\033[0m")
else:
    print("\033[31mStatus code:", status_code, "\033[0m")

# Get the XML content
xml = response.text

# Find all entries (products) in the XML
entries = re.findall("<entry>.*?</entry>", xml, re.DOTALL)

# Initialize the count of all products and the count of found products
product_count = len(entries)
found_product_count = 0

# The desired level3_category_description
desired_category = "My category name"

# Search for the desired level3_category_description in each entry
matching_entries = []
for entry in entries:
    if "<level3_category_description>" + desired_category + "</level3_category_description>" in entry:
        found_product_count += 1
        matching_entries.append(entry)

# Write the matching entries into the output.xml file
with open("output.xml", "w", encoding="UTF-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write("<product_results>\n")
    for entry in matching_entries:
        f.write("  " + entry + '\n')
    f.write("</product_results>")

# Print the result
print("\033[1mNumber of products in the XML:\033[0m", product_count)
print("\033[36mNumber of found products:\033[0m", found_product_count)

