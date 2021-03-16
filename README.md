# split_HTML_files
split HTML files using BeautifulSoup

easysplit.py splits a HTML file into separate HTML files.
It is expecting an input file called ```file_to_split.html``` in the same directory as this script
You will need to create a folder called 'pages' (because i'm too lazy to program the creation of the folder - deal with it)
```splitat``` is the variable for the string at which you want to split the HTML file
It then encloses the split block with <html><body>...</body></html> to make it a properly formatted HTML file

convert_files_html2docx.sh is a bash script that requires [Pandoc](https://pandoc.org)
to convert the html files to docx files, that were output by easysplit.py into the folder pages/
