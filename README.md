# split_HTML_files

easysplit.py splits a HTML file into separate HTML files.

## Requirements

* Python3
* an input file called ```file_to_split.html``` in the same directory as this script
* a folder named ```pages```

## Usage

Change the ```splitat``` variable to the string at which you want to split the HTML file

```python3 easysplit.py```

# convert_files_html2docx.sh

convert_files_html2docx.sh converts the html files that were output by easysplit.py and saved the folder pages/, into docx files.

## Requirements

*  [Pandoc](https://pandoc.org)

## Usage

make it executable
```chmod +x convert_files_html2docx.sh```

then to run it
```./convert_files_html2docx.sh```
