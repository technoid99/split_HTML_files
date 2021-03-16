from bs4 import BeautifulSoup

#Opens the file html_file_to_split.html
soup = BeautifulSoup(open("file_to_split.html"))

#define the string at which to split the html file
splitat = '<div class="content block">'

#put the split blocks into the folder pages. name them as reportn.html
pageNum = 0
for i in soup.prettify().split(splitat):
    f = open('pages/report' + str(pageNum) + '.html', 'w')        
    f.write('<html><body>' + splitat + ''.join(i) + '</body></html>')
    f.close()
    pageNum = pageNum + 1
