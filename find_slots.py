import requests
import datetime
import json
from time import sleep
from fake_useragent import UserAgent
from win10toast import ToastNotifier

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

### Variables

## Important Variables
# 0 = Search entire state, 1 = Search only a single district
method = 0

# Set state code or district code 0 to query state and district code list
state_code = 0
district_code = 0

# Set your age
age = 0


## Optional Variables
# Print extra information? (like slots not avaialble on XX-XX-XXXX) (0=No and 1=Yes)
print_detailed = 0

# Number of days to check in advance
numdays = 4

# Check variables
def printCodes():
    for state_code in range(1,40):
        print("State code: ", state_code)
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code),  headers=browser_header)
        json_data = json.loads(response.text)
        for i in json_data["districts"]:
            print(i["district_id"],'\t', i["district_name"])
        print("\n")
        
if method==0:
    if state_code==0:
        printCodes()
    elif state_code not in range(1,40):
        raise Exception("State code not in range: 1-40")
elif method==1:
    if district_code==0:
        printCodes()
else:
    raise Exception("Method option not in range (0-1)")



### Script
# Find today's date
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
# print(date_str)
def checkDistrict(DIST_ID):
    global print_detailed
    global age
    none_found = 1
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
        response = requests.get(URL,  headers=browser_header)
        if response.ok:
            slots_age = 0
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            if resp_json["centers"]:
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if (session["min_age_limit"] <= age) and (session["available_capacity"] > 0):
                                slots_age=1
                                none_found=0
                                print()
                                print("\t", INP_DATE)
                                print("\t", center["name"])
                                print("\t Pincode:", center["pincode"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\t Paid: ", center["fee_type"])
                                with open(f"log_of_age-{age}.log","a") as f:
                                    f.write(f"""{datetime.datetime.now()}    Date-{INP_DATE} Center- {center["name"]} Slots - {session["available_capacity"]} {session["vaccine"]}\n""")
                                try:
                                    n = ToastNotifier()
                                    n.show_toast("Vaccine Available!!!", f"""On -{INP_DATE} at- {center["name"]} slots - {session["available_capacity"]}\n {session["vaccine"]} {center["fee_type"]}""", duration = 5, icon_path ="./icon.ico",threaded=False)
                                except:
                                    pass
        else:
            print("Respose is not getting through")
        if print_detailed==1:
            if slots_age==0:
                print("\tNo available slots on {} for your age".format(INP_DATE))

    if none_found==1:
        print("\t-\tNONE.")

def createDistrictDictionary(STATE_ID):
    response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(STATE_ID),  headers=browser_header)
    json_data = json.loads(response.text)
    dict = {}
    for i in json_data["districts"]:
        dict.update({i["district_id"] : i["district_name"]})
    return dict

# Execute
while True:
    if method==1:
        checkDistrict(district_code)

    if method==0:
        dict = createDistrictDictionary(state_code)
        for i in dict.keys():
            print("\n", i, dict[i], end="")
            checkDistrict(i)

    print("\nSEARCH COMPLETE.")
    sleep(20)
