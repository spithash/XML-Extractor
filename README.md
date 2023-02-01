# XML-Extractor
An XML extractor for products matching specific elements using regular expressions written in Python.

## WHY?
I personally use this script to extract (match) products matching certain categories from an XML url containing thousands of products and get only the ones I want, the ones I select and output it in another file.

Use it to create custom (category specific) XMLs and import the products of 'output.xml' in WpAllImport.

## USAGE
Select an element (change it to match yours) like __<level3_category_description>__ for example and match products belonging to that category, editing the variable value of 'desired_category' in the lines below:
```
if "<level3_category_description>" + desired_category + "</level3_category_description>" in entry:
```
and
```
desired_category = "My category name"
```
level3_category_description is an element of a **```<product>```** entry. Selecting that and changing 'desired_category' string value __selects__ the product category. 

So if you want to select another category, you do so by changing ```desired_category = "Smartphones"```

### Sample product entry
```
<entry>
	<code>22301</code>
	<PerItemBarCode>22929</PerItemBarCode>
	<MUCode>ΤΕΜ</MUCode>
  <name>Product Name</name>
	<description>Product Description</description>
	<image>https://example.com/photos/e7207152345c.jpg</image>
	<level3_category_description>Smartphones</level3_category_description>
	<pricing_category>147-2</pricing_category>
	<quantity_mode_value>10</quantity_mode_value>
	<availability>out of stock</availability>
	<price>2.52</price>
	<recommended_retail_price_with_vat>2.03</recommended_retail_price_with_vat>
	<recommended_retail_price_no_vat>1.64</recommended_retail_price_no_vat>
	</entry>
```
### OUTPUT
The script will output matching products (or rather entries) in an XML file called **output.xml**.

Enjoy :)

