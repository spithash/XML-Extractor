import requests
import re
import time
import sys

def progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    sys.stdout.flush()
    if iteration == total: 
        print()

# Variables
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}

# Set the XML url
url = "https://www.example.com/productsxml/"

# Set the category name
desired_category = "My category name"

# Set element prefix and suffix
selectorprefix = "<level3_category_description>"
selectorsuffix = "</level3_category_description>"

print("Fetching XML data...\n")

# Request the XML from the URL
url_response = requests.get(url, headers=headers)

# Get the status code
status_code = url_response.status_code

# Color the HTTP status code message based on the value
if status_code >= 200 and status_code < 300:
    print("\033[32mStatus code:", status_code, "\033[0m")
elif status_code >= 300 and status_code < 400:
    print("\033[33mStatus code:", status_code, "\033[0m")
else:
    print("\033[31mStatus code:", status_code, "\033[0m")

# Get the XML content
xml = url_response.text

# Find all entries (products) in the XML
entries = re.findall("<entry>.*?</entry>", xml, re.DOTALL)

# Count total products and then count matching products
product_count = len(entries)
found_product_count = 0
matching_entries = []

# Search for desired element in each entry
for i, entry in enumerate(entries):
    if selectorprefix + desired_category + selectorsuffix in entry:
        found_product_count += 1
        matching_entries.append(entry)
    progress_bar(i + 1, product_count, prefix = 'Loading:', suffix = 'Complete', length = 50)
    time.sleep(0.001)

# Write the matching entries into the output.xml file
with open("output.xml", "w", encoding="UTF-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write("<product_results>\n")
    for entry in matching_entries:
        f.write("  " + entry + '\n')
    f.write("</product_results>")

print("\033[1mNumber of products in the XML:\033[0m", product_count)
print("\033[36mNumber of found products:\033[0m", found_product_count)

