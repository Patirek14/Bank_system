import pymongo
import bank_utils as bu

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["bank"]
user_table = db["pracownicy"]
client_table = db["klienci"]
init_cash = 100

x = bu.make_menu(["Zaloguj sie jako klient",
"Zaloguj sie jako pracownik",
"Dodaj klienta banku",])

def uzytkownik(client):

    while(True):
        x = bu.make_menu([
        "Stan konta","Wykonaj przelew",
        "Wyswietl historie transakcji"])

        if x == 1:
            print("Twoj stan konta wynosi: " + str(client["stan-konta"]) + " zl")
        elif x == 2:
            print("Podaj login osoby do ktorej robisz przelew: ")
            name = input() 
            client2 = client_table.find_one({"login" : name})
            print("Podaj kwote: ")
            kwota = float(input())
            aa = float(client["stan-konta"]) - kwota
            bb = float(client2["stan-konta"]) + kwota
            tmp = client["login"]
            client_table.update_one({"login" : tmp},{ "login": aa } )
            client_table.update_one({"login" : name},{ "login": bb } )

if x == 1:
    name = input("Podaj login: ")
    passwd = input("Podaj haslo: ")
    client = client_table.find_one({"login" : name })
    if not client:
        print("Nie ma takiego loginu")
    if client["haslo"] == passwd:
        print("Zostales zalogowany: " + client["login"])
        uzytkownik(client)
    else:
        print("Niepoprawne haslo")
elif x == 3:
    name = input("Podaj login: ")
    passwd = input("Podaj haslo: ")
    client = client_table.insert_one({"login":name,"haslo":passwd,"stan-konta":init_cash, "historia":{}})

    
    

    
