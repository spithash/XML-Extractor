# XML-Extractor
An XML extractor for extracting products matching specific entries using regular expressions written in Python.

I personally use this script to extract (match) certain product categories from an XML url containing thousands of products and get only the ones I want, the ones I select.

I use it to create my custom (category specific) XMLs and I import the products of 'output.xml' in WpAllImport.

Select an element like '<level3_category_description>' for example and match it's contents editing the variable value of 'desired_category'

The script will output matching products (or rather entries) in an XML file called 'output.xml'.

Enjoy :)

