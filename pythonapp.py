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
            campinfo = f"{campaign_title}:{campaign_details}:{start_date}:{end_date}:{target}\n "
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
    campaign_title = input("please enter the name of the campaign : ")
    try:
        fileobj = open("campinfo.txt", "r")
        campinfos = fileobj.readlines()
        for p in campinfos:
            campinfo = p.strip("\n")
            campinfo = campinfo.split(":")
            newline = []
            if campinfo[0] == username:
                if campinfo[1] == campaign_title:
                    while True:
                        edit = input(
                            "editing:\n 1 to edit title\n 2 to edit details\n 3 to edit start date\n 4 to edit end date\n 5 to edit target\n choose 6 if you want to exit\n")
                        if edit == "1":
                            oldtitle = campinfo[1]
                            newtitle = input(" please enter new campaign title : ")
                            newline.append(p.replace(oldtitle, newtitle))
                            with open("campinfo.txt", "w") as f:
                                for line in newline:
                                    f.writelines(line)
                                    print("campaign title updated sucessfully")
                        elif edit == "2":
                            olddetails = campinfo[2]
                            newdetails = input(" please enter new campaign details : ")
                            newline.append(p.replace(olddetails, newdetails))
                            with open("campinfo.txt", "w") as f:
                                for line in newline:
                                    f.writelines(line)
                                    print("campaign details updated sucessfully")
                        elif edit == "3":
                            old_start_date = campinfo[3]
                            new_start_date = input(" please enter new campaign's start date : ")
                            newline.append(p.replace(old_start_date, new_start_date))
                            with open("campinfo.txt", "w") as f:
                                for line in newline:
                                    f.writelines(line)
                                    print("campaign's start date updated sucessfully ")
                        elif edit == "4":
                            old_end_date = campinfo[4]
                            new_end_date = input(" please enter new campaign's end date : ")
                            newline.append(p.replace(old_end_date, new_end_date))
                            with open("campinfo.txt", "w") as f:
                                for line in newline:
                                    f.writelines(line)
                                    print("campaign's end date updated sucessfully")
                        elif edit == "5":
                            oldtarget = campinfo[5]
                            newtarget = input(" please enter new campaign target : ")
                            newline.append(p.replace(oldtarget, newtarget))
                            with open("campinfo.txt", "w") as f:
                                for line in newline:
                                    f.writelines(line)
                                    print("campaign target updated sucessfully")
                        elif edit == "6":
                            break
                        else:
                            print("invalid input")
                            edit = input(
                                "editing:\n 1 to edit title\n 2 to edit details\n 3 to edit start date\n 4 to edit end date\n 5 to edit target\n choose 6 if you want to exit\n")

                else:
                    print(f" user {projectinfo[0]} don't have any projects with name {projectname} please try again")
                break
    except(Exception):
        print(" no project found ")

#####################################################################################

def delete_campaign():
    fileobj = open("campinfo.txt", "r")
    users = fileobj.readlines()

    with open("campinfo.txt", "w") as f:
        for u in users:
            usrinfo = u.strip("\n")
            userinfo = usrinfo.split(":")
            if userinfo[1] == project_name in u:
                f.write(" \n")
            else:
                f.write(u)

##############################################################################

def campaign_main_menu():
    campaign_menu = input("press 1 to create campaign\n press 2 to view campaigns\n press 3 to edit campaign\n press 4 to delete campaign")
    if campaign_menu == "1":
        create_campaign()
    if campaign_menu == "2":
        view_campaigns()
    if campaign_menu == "3":
        edit_campaign()
    if campaign_menu == "4":
        delete_campaign()
    else:
        exit()

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
            usersinfo = f"{first_name}:{last_name}:{email}:{password}:{phone}\n "
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
    login_or_rigister = input("press 1 if you want to login\n press 2 if you want to register")
    if login_or_rigister == "1":
        login()
    if login_or_rigister == "2":
        register()
    else:
        continue


### user after registration should login to be able to view campaign main menu