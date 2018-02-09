#This Program appends 'https://www.gamestop.com' to the beginning of each
#of the partial urls in the xboxOneUrls.txt file

gamestopBeg = 'https://www.gamestop.com'

linksXboxOne = open('xboxOneUrls.txt', 'r')

for line in linksXboxOne:
    f = open('realXboxOneUrls.txt','a')
    f.write(gamestopBeg + line)
    print(line)
    f.close
    
