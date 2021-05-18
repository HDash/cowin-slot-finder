from logging import exception
import requests
import datetime
from time import sleep
from fake_useragent import UserAgent

temp_user_agent = UserAgent()
browser_header = {'User-Agent': temp_user_agent.random}

### Variables

## Important Variables
# 0 = Search entire state, 1 = Search only a single district
method = 1

# Set pincode
Pin_Code = int(input("Enter a valid Pin: "))

# Set your age
age = int(input("Enter Your Age: "))


## Optional Variables
# Print extra information? (like slots not avaialble on XX-XX-XXXX) (0=No and 1=Yes)
print_detailed = 0

# Number of days to check in advance
numdays = 4


### Script
# Find today's date
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
# print(date_str)
def ageCalculator(age):
    if age<45 and age>=18:
        return 18
    if age>45:
        return 45
    else:
        return 0   


def checkSlot(pin):
    global print_detailed
    global age
    none_found = 1
    for INP_DATE in date_str:
        URL = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pin}&date={INP_DATE}"
        response = requests.get(URL,  headers=browser_header)
        if response.ok:
            slots_age = 0
            resp_json = response.json()

            if resp_json["sessions"]:
                    for session in resp_json["sessions"]:
                        if (session["min_age_limit"] == ageCalculator(age)) and (session["available_capacity"] > 0):
                            slots_age=1
                            none_found=0
                            print()
                            print("\t", INP_DATE)
                            print("\t", session["name"])
                            print("\t Pincode:", session["pincode"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if(session["vaccine"] != ''):
                                print("\t Vaccine: ", session["vaccine"])
                            print("\t Paid: ", session["fee_type"])
                            with open(f"log_of_age-{age} pin- {pin}.log","a") as f:
                                f.write(f"""{datetime.datetime.now()}    Date-{INP_DATE} Center- {session["name"]} Slots - {session["available_capacity"]} {session["vaccine"]}\n""")
        else:
            print("Respose is not getting through or invalid pin")
        if print_detailed==1:
            if slots_age==0:
                print("\tNo available slots on {} for your age".format(INP_DATE))

    if none_found==1:
        print("\t-\tNONE.")


# Execute
while True:
    if method==1:
        checkSlot(Pin_Code)

    print(f"\nSEARCH COMPLETE. at {datetime.datetime.now()} ")
    sleep(20)
