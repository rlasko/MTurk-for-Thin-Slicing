import json
import requests
import pprint
import csv
import random

apiKey = "ba583d77831a196b0cc9ba1fefd4bc16" # replace with account's API key

filenameAmazon = "MTurkCSVFile" # optionally change to desired filename
filenameAnalysis = "videoNameRef" # optionally change to desired filename

parameter = {"SproutVideo-Api-Key":apiKey}

url ="https://api.sproutvideo.com/v1/videos"

r = requests.get(url, headers=parameter) # get data from sproutvideo

pythonData = r.json() # convert to python readable data

# pp = pprint.PrettyPrinter(indent=4) # use this to print things nicely

videos = pythonData["videos"] # access video portion of data

urlList = []
refList = []

# iterate through all videos and get video link (url) and src to embed
for video in videos:
    # get URL
    assets = video['assets']
    videoLink = assets['videos']
    title = video['title']
    print(title)

    # get SRC
    embedCode = video['embed_code']
    srcIndex = embedCode.find("src")
    srcLinkStart = srcIndex + 5
    srcLinkEnd = embedCode.find("'",srcLinkStart)
    src = "https:" + embedCode[srcLinkStart:srcLinkEnd] # add prefix to src

    # add to list
    urlList.append(src)
    refList.append((title, src))

try:
    assert(len(urlList) == len(refList))
except:
    print("Hmm something went wrong. Check the input")
    
random.shuffle(urlList) # randomize list

# write to file - data for MTurk
csvFile = open(filenameAmazon + ".csv", "w")
csvFile.write('src')
csvFile.write('\n')
for src in urlList:
    csvFile.write(src)
    csvFile.write('\n')
csvFile.close()

# write reference file to match MTurk data to video num later
csvFile = open(filenameAnalysis + ".csv", "w")
csvFile.write('title' + ',' + 'src')
csvFile.write('\n')
for title,src in refList:
    csvFile.write(title + ',' + src)
    csvFile.write('\n')
csvFile.close()
