import re

email_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
date_regex = re.compile("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$")     #dd/mm/yyyy

################################################################

def check_user_input(input):
    try:
        #convert it into integer
        val = int(input)
        return "number"
    except ValueError:
        try:
            #convert it into float
            val = float(input)
            return "float"
        except ValueError:
            return "string"

#############################################################################

def isValid(email):
    if re.fullmatch(email_regex, email):
        return True

    print("Invalid email")
    return False

def checkstartdate(start_date):
    if re.fullmatch(date_regex, start_date):
        return True

    print("wrong date format")
    return False

def checkenddate(end_date):
    if re.fullmatch(date_regex, end_date):
        return True

    print("wrong date format")
    return False

##################################################3

def create_campaign():
    campaign_title = input("please enter your campaign title : ")
    while check_user_input(campaign_title) != "string" or not campaign_title:
        print("please enter a valid name \nNOTE : don't use numbers or empty value")
        campaign_title = input("please enter your campaign title : ")

    campaign_details = input("please enter your campaign details : ")
    while check_user_input(campaign_details) != "string" or not campaign_details:
        print("please enter a valid name \nNOTE : don't use numbers or empty value")
        campaign_details = input("please enter your campaign details : ")

    start_date = input("please enter your start date in this format dd/mm/yyyy : ")
    while (not checkstartdate(start_date)):
        start_date = input("please enter your start date in this format dd/mm/yyyy : ")

    end_date = input("please enter your end date in this format dd/mm/yyyy : ")
    while (not checkenddate(end_date)):
        end_date = input("please enter your end date in this format dd/mm/yyyy : ")

    target = input("please enter your target : ")
    while check_user_input(target) != "number" or target == False:
        print("please enter a valid target  \nNOTE : don't use letters or empty value")
        target = input("please enter your target : ")

    while True:
        done = input("please enter done to create campaign : ")
        if done == "done":
            fileobj = open("campinfo.txt", "a")
            campinfo = f"{campaign_title}:{campaign_details}:{start_date}:{end_date}:{target} \n "
            fileobj.write(campinfo)
            fileobj.close()
            print(" campaign created successfully <3 ")
            break

###############################################################################################

def view_campaigns():
    fileobj = open("campinfo.txt", "r")
    print(fileobj.read())
    fileobj.close()

##############################################################################################

def edit_campaign():

#####################################################################################

def delete_campaign():

##############################################################################

def campaign_main_menu():
    campaign_menu = input("press 1 to create campaign \n press 2 to view campaigns \n press 3 to edit campaign \n press 4 to delete campaign")
    if campaign_menu == "1":
        create_campaign()
    if campaign_menu == "2":
        view_campaigns()
    if campaign_menu == "3":
        edit_campaign()
    if campaign_menu == "4":
        delete_campaign()
    else:
        breakpoint()

##########################################################################################################

def register():
    first_name = input("please enter your first name : ")
    while check_user_input(first_name) != "string" or not first_name:
        print("please enter a valid name \nNOTE : don't use numbers or empty value")
        first_name = input("please enter your first name : ")

    last_name = input("please enter your last name : ")
    while check_user_input(last_name) != "string" or not last_name:
        print("please enter a valid name \nNOTE : don't use numbers or empty value")
        last_name = input("please enter your last name : ")

    email = input("please enter your email : ")
    while (not isValid(email)):
        email = input("please enter your email : ")

    password = input("please enter your password : ")
    confirm_password = input("please confirm your password : ")
    while password != confirm_password:
        print("password not match")
        confirm_password = input("please confirm your password : ")

    phone = input("please enter your phone number : ")
    while check_user_input(phone) != "number" or phone == False:
        print("please enter a valid phone number  \nNOTE : don't use letters or empty value")
        phone = input("please enter your phone number : ")

    while True:
        done = input("please enter done to create account : ")
        if done == "done":
            fileobj = open("usersinfo.txt", "a")
            usersinfo = f"{first_name}:{last_name}:{email}:{password}:{phone} \n "
            fileobj.write(usersinfo)
            fileobj.close()
            print(" account created successfully <3 ")
            break

#####################################################################

def login():
    email = input("please enter your email : ")
    while not isValid(email):
        email = input("please enter your email : ")

    password = input("please enter your password : ")

    while True:
        ok = input("please enter ok to login: ")
        if ok == "ok":
            fileobj = open("usersinfo.txt", "r")
            users = fileobj.readlines()
            for u in users:
                userinfo = u.strip("\n")
                userinfo = userinfo.split(":")
                if userinfo[2] == email and userinfo[3] == password:
                    print(f"welcome back {userinfo[0]}  <3 ")
                    campaign_main_menu()
                    break
                else:
                    print(
                        " wrong email or password please try again \n if tou don't have account please register first ")
                    break
            break
        else:
            continue

#################################################################

while True:
    login_or_rigister = input("press 1 if you want to login \n press 2 if you want to register")
    if login_or_rigister == "1":
        login()
    if login_or_rigister == "2":
        register()
    else:
        continue


### user after registration should login to be able to view campaign main menu