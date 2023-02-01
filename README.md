# XML-Extractor
An XML extractor for products matching specific elements using regular expressions written in Python.

## WHY?
I personally use this script to extract (match) products matching certain categories from an XML url containing thousands of products and get only the ones I want, the ones I select and output it in another file.

Use it to create custom (category specific) XMLs and import the products of 'output.xml' in WpAllImport.

## USAGE
Select an element (change it to match yours) like __<level3_category_description>__ for example and match products belonging to that category, editing the variable value of 'desired_category' in the line below:
```
if "<level3_category_description>" + desired_category + "</level3_category_description>" in entry:
```
and
```
desired_category = "My category name"
```
This is an element of a <product>. Selecting that and changing 'desired_category' string value __selects__ the product category. 

So if you want to select another category, you do so by changing ```desired_category = "Smartphones"```

### OUTPUT
The script will output matching products (or rather entries) in an XML file called 'output.xml'.

Enjoy :)

