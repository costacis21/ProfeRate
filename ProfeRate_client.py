import requests
import json
import pandas as pd
from tabulate import tabulate

if __name__=="__main__":
    command=""
    url=""
    while command!="exit":
        appurl = "/api/"
        command=""
        command = input('Enter command: ')
        if (command == "register"):
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")
            uri=url+appurl+command
            r = requests.post(uri, data={'username': username,'password':password,'email':email})

        elif (command.split(" ")[0] == "login" and len(command.split(" "))>1):
            username = input("Username: ")
            password = input("Password: ")
            url = command.split(" ")[1]
            # url='http://localhost:8000'
            uri=url+appurl+command.split(" ")[0]
            try:
                r = requests.post(uri, data={'username': username, 'password': password})
                print(r.text)
            except requests.exceptions.RequestException:
                print("Couldn't reach server")


        elif (command == "logout" and url!=''):
            uri=url+appurl+command
            try:
                r = requests.post(uri)
                print(r.text)
            except requests.exceptions.RequestException:
                print("Couldn't reach server")
            url=''



        elif (command == "list" and url!=''):
            uri=url+appurl+command
            r = requests.post(uri)
            ratingstmp = (json.loads(r.text))
            ratings = []
            for rating in ratingstmp:
                ratings.append(rating['fields'])
            df = pd.DataFrame(ratings)
            print(tabulate(df, headers="keys"))



        elif (command == "view" and url!=''):
            uri=url+appurl+command
            r = requests.post(uri)
            try:
                ratings=(json.loads(r.text))
                df = pd.DataFrame(ratings)
                print(tabulate(df, headers="keys"))
            except:
                print("something went wrong")



        elif command.count(" ")>0 and url!='':
            req= command.split(" ")

            if(req[0]=="average" and len(req)==3):
                uri = url + appurl + req[0]
                r = requests.post(uri, data={'professor_id': req[1], 'module_code': req[2]})
                with open("response.html", "wb") as f:
                    f.write(r.content)
                response=json.loads(r.text)
                if 'rating' in response[0]:
                    print(f"The rating of {response[0]['name']} ({response[0]['name_code']}) in module {response[0]['module_name']} ({response[0]['module_code']}) is {response[0]['rating']}")
            if (req[0] == "rate" and len(req)==6):
                # rate professor_id module_code year semester rating
                uri = url + appurl + req[0]
                r = requests.post(uri, data={'professor_id': req[1], 'module_code': req[2], 'year':req[3], 'semester':req[4], 'rating': req[5]})
                print(r.text)
        elif command == "help":
            print("OPTIONS:\n\tlogin [url]\n\tregister\n\tlogout\n\tlist\n\tview\n\taverage [professor_id] [module_code]\n\trate [professor_id] [module_code] [year] [semester] [rating]")



