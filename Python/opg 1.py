
# %% opg 1
a = "Hello, World!"
b = "vh. Frederik"
print(a)
print(b)

# %% opg 2
navn = str("Frederik")      # str
alder = int(28)             # int
temperatur = float(-500.5)  # float
studerende = bool(True)     # bool

print("Mit navn er {}, jeg er {} år og temperaturen er {}°C".format(navn, alder, temperatur))

# %%
a = float(input("Indtast 1. tal: "))
b = float(input("Indtast 2. tal (b): "))
plus = a + b
minus = a - b
gange = a * b
dividere = a / b if b != 0 else "Uendelig (kan ikke dividere med nul)"
print(f"{a} + {b} = {plus}")
print(f"{a} - {b} = {minus}")   
print(f"{a} * {b} = {gange}")
print(f"{a} / {b} = {dividere}")

if a > b:
    print (f"{a} er større end {b}")
elif a < b:
    print(f"{a} er mindre end {b}")
else:
    print(f"{a} er lig med {b}")

# %%
def læs_tal(prompt):
    while True:
        try:
            return float(input(prompt))   # eller int(), hvis du kun vil have heltal
        except ValueError:
            print("OMMER, DU SKAL INDTASTE EN TEMPERATUR!")


a = float(input("Indtast temperatur i °C: "))

if a < 0:
    print ("DET ER FROSTVEJR!")
elif 0 <= a <= 10:
    print("Det er koldt!")
elif 10 < a <= 20:
    print("Det er mildt vejr")
elif 20 < a:
    print("Det er alt alt alt for varmt!")


# %%

liste = [3, 7, 2, 9, 4]


sum_liste = 0
for l in liste:
    print(l)
    sum_liste += t

print(f"Summen af tallene er: {sum_liste}")

i = 10
while i >= 0:
    print(i)
    i -= 1
print (liste)

# For-loop: udskrive kun tal større end 5
print("Tal større end 5:")
for l in liste:
    if l > 5:
        print(l)


# %%
temperaturer = [21.5, 22.0, 21.5, 23.1, 22.0]
sensorer = {
    "sensor_1": 21.5,
    "sensor_2": 22.0,
    "sensor_3": 21.5,
    "sensor_4": 23.1,
    "sensor_5": 22.0
}
unikke_temperaturer = set(temperaturer)


print("Alle temperaturer i listen:")
for temp in temperaturer:
    print(temp)

# --- Udskriver alle sensorer og deres værdi ---
print("\nSensorer og deres seneste målinger:")
for sensor, værdi in sensorer.items():
    print(f"{sensor}: {værdi}")

# --- Udskriver alle unikke temperaturer ---
print("\nUnikke temperaturer:")
for temp in unikke_temperaturer:
    print(temp)

# %%
tekst = "  Hello, World!  "


print("Original tekst:", repr(tekst))
print("Uppercase:", tekst.upper())
print("Lowercase:", tekst.lower())
print("Strip:", tekst.strip())
print("Replace:", tekst.replace("World", "Python"))
print("Split:", tekst.split(","))

# Liste med ord og join
ord = ["hindbærsnitter", "er", "lækkert"]
samlet = " ".join(ord)
print("Samlet streng fra liste:", samlet)

# Slicing: udskriver kun 'Hello'
ren_tekst = tekst.strip()
print("Slicing 'Hello':", ren_tekst[])

# %%
# functions.py
navn = "Frederik"
liste = [10, 15, 20, 25, 30, 35, 40, 50]

# Funktion der returnerer summen af to tal
def add(a, b):
    return a + b

# Funktion der returnerer True, hvis tallet er lige
def is_even(n):
    return n % 2 == 0

# Funktion der printer en hilsen
def greet(navn):
    print(f"Hej {navn}!, Du ser godt ud i dag!")

# Ekstra: Funktion der beregner gennemsnittet af en liste tal
def average(liste):
    if len(liste) == 0:
        return 0  # undgår division med nul
    return sum(liste) / len(liste)

# Main-sektion
if __name__ == "__main__":
    # Test add
    resultat = add(5, 7)
    print(f"5 + 7 = {resultat}")

    # Test is_even
    tal = 8
    print(f"{tal} er lige:", is_even(tal))
    tal = 3
    print(f"{tal} er lige:", is_even(tal))

    # Test greet
    greet("Frederik")

    # Test average
    
    print(f"Gennemsnittet af {liste} er {average(liste)}")


# %%
import time

Velkomstbesked = "Velkommen til mit program!"
print(Velkomstbesked)

def menu():
    print("\nMenu:")
    print("1. Hej_funktion")
    print("2. Vis nuværende tid")
    print("3. Afslut")

def hej():
    navn = input("Indtast dit navn: ")
    print(f"Hej, {navn}!")


def vis_tid():
    nu = time.localtime()
    tid_str = time.strftime("%H:%M:%S", nu)
    print("Nuværende tid:", tid_str)

def farvel():
    svar = input("Var du tilfreds med oplevelsen? (Ja/Nej): ").strip().lower()
    if svar == "ja":
        print("Tak for feedback! Farvel!")
    elif svar == "nej":
        print("Lev med det")
    else:
        print("Ugyldigt svar. Farvel!")


if __name__ == "__main__":
    while True:
        menu()
        valg = input("Vælg en mulighed (1-3): ")

        if valg == "1":
            hej()
        elif valg == "2":
            vis_tid()
        elif valg == "3":
            farvel()
            break
    else:
        print("Ugyldigt valg, prøv igen.")  


# %%
import random

tal = random.randint(1, 20)

for forsøg in range(1, 6):
    gæt = int(input(f"Forsøg {forsøg}: Gæt et tal mellem 1 og 20: "))
    
    if gæt == tal:
        print("Tillykke! Du burde tage på kasino!")
        break
    elif gæt < tal:
        print("For lavt!")
    else:  # gæt > tal
        print("For højt!")
else:
    print(f"Du elendig! Tallet var {tal}.")


# %%
import requests

url = "https://www.elprisenligenu.dk/api/v1/prices/2025/11-24_DK1.json"

response = requests.get(url)

print("Statuskode:", response.status_code)

data = response.json()  # JSON -> dict

for time in data:
    print(time["time_start"], "-", time["time_end"])
    print("DKK_per_kWh:", time["DKK_per_kWh"])
    print("EUR_per_kWh:", time["EUR_per_kWh"])
    print("EXR:", time["EXR"])
    print("---")

# %%
import requests

url = "http://api.currencylayer.com/live"
params = {
    "access_key": "5fac735115a2d19d4f15b446b8b69bf6",
    "source": "USD",
    "currencies": "EUR",
    "format": 1
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Rå data:", data)

    # Hent valutakurser
    quotes = data.get("quotes", {})
    for key, value in quotes.items():
        print(f"{key}: {value}")
else:
    print("Fejl i API-kaldet:", response.status_code)


# %%
import requests

url = "https://api.currencylayer.com/list"
params = {
    "access_key": "5fac735115a2d19d4f15b446b8b69bf6"
}

response = requests.get(url, params=params)

print("Statuskode:", response.status_code)  # Skal være 200
print("Rå tekst:", response.text)           # Se hvad API faktisk sender
# %%
