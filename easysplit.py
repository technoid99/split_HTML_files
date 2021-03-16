from bs4 import BeautifulSoup

#Opens the file html_file_to_split.html
soup = BeautifulSoup(open("file_to_split.html"))

#splits it at the search string <div class="content block"> in the HTML file
#adds <div class="content block"> back in and saves that block as a single html file in pages/
#repeat
pageNum = 0
for i in soup.prettify().split('<div class="content block">'):
    f = open('pages/report' + str(pageNum) + '.html', 'w')        
    f.write('<html><body><div class="content block">' + ''.join(i) + '</body></html>')
    f.close()
    pageNum = pageNum + 1
