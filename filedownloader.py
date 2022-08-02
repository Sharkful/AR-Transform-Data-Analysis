import requests, re

# URL to pull logs from
base_url = "http://cyberlearnar.cs.mtsu.edu/show_uploaded/DeviceLogs/07-05-2022/"

# List of log filenames, line separated
filelist = open("filelist.txt")
filenames = filelist.readlines()

# Downloadthe files one at a time
for filename in filenames:
    # Construct the URL and download the log
    filename = filename.strip()
    url = base_url + filename
    response = requests.get(url)
    # Build a new, shorter filename
    newFilename = re.search("User_\d+", filename).group()
    if re.search("Transform", filename) == None:
        newFilename += ".log"
    else:
        newFilename += "_TransformTracking.dat"
    
    # write the downloaded log to a local file
    with open("Data/" + newFilename, "wb") as file:
        file.write(response.content)