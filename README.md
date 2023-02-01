# XML-Extractor
An XML extractor for products matching specific entries using regular expressions written in Python.

## WHY?
I personally use this script to extract (match) products matching specific categories from an XML url containing thousands of products and get only the ones I want, the ones I select.

Use it to create custom (category specific) XMLs and import the products of 'output.xml' in WpAllImport.

## USAGE
Select an element like '<level3_category_description>' for example and match it's contents editing the variable value of 'desired_category' in the line below:
```
if "<level3_category_description>" + desired_category + "</level3_category_description>" in entry:
```
This is an element of a <product>. Selecting that and changing 'desired_category' string value __selects__ the product category. 

### OUTPUT
The script will output matching products (or rather entries) in an XML file called 'output.xml'.

Enjoy :)

