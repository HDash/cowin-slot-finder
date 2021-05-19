# CoWin Slot Finder - (Pythonic way to search)
An automated tool/Script/Application to find available slots for your age and state/district and pin using CoWin API.

[Cowin](cowin.gov.in) is the portal for pan-India Covid-19 vaccination drive.

**How is it different from others?**  
- Saves your precious time
- No installation required for windows distributions
- Can find slot by Postal Pin code
- Can find slot as per your dose requirement (i.e. First or Second Dose) so no false alarm
- Easy to use and lightweight
- Continuous tracking of slot. No need of user attention after setup.
- Updates data 3 times in a minute and send you a notification on your notification panel.

This script can search through the entire state and organize the results as per district and date. Moreover, it only shows centres with available slots (prevents clutter). Also in Windows 10 systems it is able to send a notification to the user. You don't need to look at the command line for the whole day.

## Screenshot
##### Working of main script find_slots.py
![Searching entire Delhi](https://i.imgur.com/XfdxlW0.png "Searching entire Delhi")
##### CLI application Searching by PIN
![CLI application Searching by PIN](https://i.imgur.com/79TkEr4.png "CLI application Searching by PIN")
##### CLI application Searching by state and district code
![CLI application Searching by state and district code](https://i.imgur.com/VnIBRck.png "CLI application Searching by state and district code")
 
# Instructions
### Users with Windows OS
- Download an exe file from the link as per your requirement [Download Releases](https://github.com/sridharjena97/cowin-slot-finder/releases/tag/1.0)
- Doubble click on application to start
- Follow the app instructions. Learn More about usage[Here](https://sridhwork.blogspot.com/2021/05/cowin-slot-booking-software.html)
- Tip: If you download the icon along with the executable and place it in same file. Notification will look more beautiful.
### Users with python 3.0 or grater on any operating system
- Download Any of the CLI application
- Follow the instructions Learn More about usage[Here](https://sridhwork.blogspot.com/2021/05/cowin-slot-booking-software.html)
### For Advanced Users Having python Installed
1. Download find_slots.py or clone the repo. 
2. Edit variables in the said file.
3. Run, using the instructions below.

## Windows
- Install latest Python form this [link](https://www.python.org/downloads/windows/).
or 
```sh
choco install python
```
- Open command prompt (cmd) and run the following-

```cmd
py -m pip install requests
py "(location)\find_slots.py"
```
or 
-You can install all dependencies from repo location using below command.
```sh
py -m pip install -r requirements.txt
```
## Linux
```cmd
sudo apt-get install python3
git clone https://github.com/HDash/cowin-slot-finder.git
pip install -r requirements.txt
python3 <script you want to run>
```

# Contribution
Feel free to pull requests.
Share your feedback and suggestions.

# Scopes of Developments
- GUI Application
- Mobile Application
 
# Credits
> [bhattbhavesh91](https://github.com/bhattbhavesh91/cowin-vaccination-slot-availability/blob/main/cowin-api-availability.ipynb) for json Parsing and request script 
> [SridharJena](https://github.com/sridharjena97) For developing CLI applications
![GitHub](https://icons.iconarchive.com/icons/danleech/simple/128/github-icon.png)

# License

MIT

**Free Software, Hell Yeah!**