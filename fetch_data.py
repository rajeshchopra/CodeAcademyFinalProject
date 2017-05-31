"""
This program fetches data from web
and removes any non-text data such as html tags
then saves to a physical file
"""
DATAFILENAME = "data.txt"

from bs4 import BeautifulSoup
import urllib2

response = urllib2.urlopen('http://gutenberg.org')
html = response.read()

# clean data by removing html tags and retaining only text
soup = BeautifulSoup(html, 'html.parser')
stripped_html_doc = soup.get_text()
print stripped_html_doc
# write data to file
with open(DATAFILENAME, "w") as cleaned_data_file:
	cleaned_data_file.write(stripped_html_doc)
	
if  cleaned_data_file.closed != True:
    cleaned_data_file.close()

