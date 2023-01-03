import requests, re
from os.path import exists

# URL to pull logs from
base_url = "https://cyberlearnar.cs.mtsu.edu/show_uploaded/"

# List of log filenames, line separated
filelist = open("../Data/recentLogs.txt")
filenames = filelist.readlines()

# Downloadthe files one at a time
for filename in filenames:
    # Construct the URL and download the log
    filename = filename.strip()
    url = base_url + filename
    print(url)
    response = requests.get(url)
    # Build a new, shorter filename
    newFilename = ""
    re_search = re.search("User_\d+", filename)
    if re_search != None: # If this is not Guest_Guest
        newFilename = re_search.group()
        if re.search("Transform", filename) == None:
            newFilename += ".log"
        else:
            newFilename += "_TransformTracking.dat"
    else: # This is Guest_Guest
        newFilename = filename

    
    # write the downloaded log to a local file
    fp = "../Data/RawLogs/" + newFilename
    if not exists(fp):
        with open(fp, "wb") as file:
            file.write(response.content)
    else:
        print(f"File already exists: {fp}")