# Access-values-from-Google-Spreadsheets
So the problem I faced with google spreadsheets was I wasnt able to get the values saved in them as a JSON, nor did I want to get in the hassles of going through the API of Google Spreadsheets, because the only thing I wanted to do was access the data from my spreadsheet (My spreadsheet contained latitude and longitude values) and plot them on a map. Thats it!

One thing I noticed is that we can publish our spreadsheet as a CSV, and once published the link directly lets us download the CSV file. So now since we have the CSV file with us we can simply use AJAX to access it. Simple right?

The **downloader.py** is a simple script which lets you download the CSV file into your working directory.
The **index.html** displays a map with markers set at latitude and longitude as obtained from the CSV file.


**Steps** you might want to follow if you want to display markers as well:
- Publish your spreadsheet. File > Publish > Select CSV from the dropdown 
- Get and Google Maps API and enable it [https://developers.google.com/maps/] [https://developers.google.com/maps/documentation/javascript/]

**Changes in downloader.py**
- Add in the url of your CSV file (you get this when you publish)

**Changes in index.html**
- Add in the Google Maps API Key in the url
- Modify the index value based upon the column number from your spreadsheet

Thats it! Now when you run the **index.html** file it will display a map with markers. *It does support multiple markers as well.*

Cheers :D
