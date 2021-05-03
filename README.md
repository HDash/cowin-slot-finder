# (Yet Another) Cowin Slot Finder - Python Edition
Simple script to find available slots for your age and state/district using Cowin API.

[Cowin](cowin.gov.in) is the portal for pan-India Covid-19 vaccination drive.

**How is it differnet from others?**  
This script can search through the entire state and organize the results as per district and date. Moreover, it only shows centres with available slots (prevents clutter).

## Screenshot
![Searching entire Delhi](https://i.imgur.com/XfdxlW0.png "Searching entire Delhi")
 
# Instructions
1. Download find_slots.py, or clone repo.
2. Edit variables in the said file.
3. Run, using the instructions below.

## Windows
1. Install latest [Python](https://www.python.org/downloads/windows/).
2. Open command prompt (cmd) and run the following-
```cmd
py -m pip install requests
py -m pip install pandas
py "(location)\find_slots.py"
```

## Linux
Well, you already know.	

# Contribution
Feel free to pull requests.
I'm very new to coding and git so I'm absolutely open to feedback and sugggestion. :)
 
# Credits
[bhattbhavesh91](https://github.com/bhattbhavesh91) - [Backend](https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/cowin-api-availability.ipynb)
