Terminology:
AMT - Amazon Mechanical Turk
HIT - Human Intelligence Task
Turker - Amazon worker that completes HITs


This package contains:
1. Script to get url from video host website
2. HTML file for Amazon HIT


Overview:
The HTML file included in this folder contains variables in the format "${url}"
The CSV file outputted by the script has headers that match the variables in the HTML file ("url")
When you create a batch on AMT, Amazon takes each of the entries in your CSV files and creates a HIT. This allows you quickly create multiple very similar HITs (in this case, everything is the same but the video each time)
The assignment number determines the number of times each HIT is available to workers. Amazon ensures that each of these repeat HITs are completed by unique Turkers, which allows the researcher to aggregate results from many raters.
If you decide to modify the format of the provided HTML file and add more variables, Be sure that each of your headers have the same number of entries (since each line corresponds to a HIT)
My video script outputs 2 files. One for Amazon, and the other that references urls to video titles. This will allow you to map the HIT results to their corresponding videos if necessary.


Tips:
After the HITs are completed, remove the videos from SproutVideo, or add a password to the embedded video. This provides security for the subjects so that Turkers are unable to access the videos again.
Choosing a higher number of assignments will allow you to average and compare them, as well as remove extremes for more reliability. (Ex: if there are 5 assignments and three ratings of 7, one of 6, and one of 1, it's fairly safe to assume that the person who rated 1 wasn't paying attention, or at least shouldn't be rating more videos)

Dependencies:
The script was written in Python3. If you do not have Python3 installed follow the instructions at python.org/downloads/release/python-351 and download Python 3.5.1

To receive data from SproutVideo, the script uses Requests, a HTTP library for Python
To install:
1. If pip is not already installed follow the instructions here https://pip.pypa.io/en/stable/installing/ to download
2. In terminal, type “pip3 install requests” (no quotes)
3. This should properly install Requests. If not, try “sudo pip3 install requests”
4. Verify that Requests was properly installed by typing “python3” into terminal, then “import re	quests” in the python command line. If no errors are thrown, you’re good to go. 


To set up Mechanical Turk HIT:

Part 1: Video Hosting
1. Set up an account on SproutVideo (sproutvideo.com). It can be any video hosting site, but I've found this to be the cheapest and most convenient for our research purposes, and my script is written for this site.
2. Upload videos. This may take some time.
3. Verify that the videos have been uploaded and processed by clicking the button to see your videos. If any still have a spinner on them, SproutVideo is still processing them.
4. Go to settings and click "API". Copy and paste your API key into the correct line in the "sproutVideoAPIScraper.py" file. (The variable is called "apiKey, just replace my string with yours")
5. The script will output two files. There are default names set, but if you'd like to change them, simply change the value of the two filename______ variables
6. Open terminal and run the script (python 3). This will save the two output files into this folder

Part 2: Amazon
1. If testing: Set up a requesters sandbox for testing purposes (workersandbox.mturk.com) Else: set up requester account (mturk.com) (Skip if you have a sandbox account already.)
2. Click "Get Started" on the right to start as a Requester
3. Switch to the create tab
4. Choose "Other" and click "Create Project"
5. Set up the HIT by setting a title and descriptions.
6. Choose a reward for the assignment. Past annotation/research projects have suggested $7-10 hourly rate
7. Enter the desired number of assignment. This determines the number of unique Turkers who will complete each HIT. This will allow you to aggregate results later and remove extremes if so desired.
8. Set worker requirements. Studies I've come across have suggested that requiring "Master" workers is unnecessary, instead set hit approval rate to 97 or 98 percent.
9. Continue to design layout. Click source to see the source code and replace all of the code there with the HTML code from the file in this folder.
10. Click "Preview" and verify that the page is laid out correctly. The video will display an error, but it's fine since we haven't given them a URL yet.
11. Click "Finish". This will take you back to the Create tab. You should see your project displayed there.
12. Click "Publish Batch". Navigate to the Amazon file outputted by the script. (It's by default named "MTurkCSVFile.csv" unless you changed it in Part 1 Step 5). Let Amazon verify the file then click upload
13. Let the file load then preview the HIT. Make sure the video is displayed correctly then click "Next"
14. Verify the values on the page, change them if necessary by going back to Create tab and clicking "Edit"
15. Otherwise click "Publish Batch" and wait for HITs to be completed.
16. To view progress, go to Manage. Here you can also download a CSV file with results and accept and reject HITs


Rejecting HITs:
After the HITs are completed, you'll want to go through them and reject the results that don't seem accurate.
Some studies suggest a "gold-standard" set of data that's completed by in-lab researchers. Mix these in with the other videos, and the Turkers that miss these ratings wildly can be considered inaccurate, and the rest of their results removed.
One heuristic that's easy to use is time. In this case, since we are using a 30 second video, if the person took less than 35 seconds to complete the HIT, we can reject their results since they probably didn't watch the whole video (consider time to watch, click 2 buttons, then press submit)
If the person selected the option that the video did not appear, you are NOT allowed to reject the HIT, per Amazon's policy. It's considered an error on our part. That result should be excluded from the results but you MUST APPROVE the HIT.

contact Rae Lasko @ rlasko.cmu.edu for clarification or questions
