webshop_produkte = [
    {"name": "USB-Kabel", "aktiv": True},
    {"name": "Alte Tastatur", "aktiv": False},  # Nicht aktiv!
    {"name": "Webcam", "aktiv": True},
    {"name": "Auslaufmodell Mousepad", "aktiv": False} # Nicht aktiv!
]

def finde_aktive_produkte(produkt_liste):
    aktive = []  # Name angepasst
    for item in produkt_liste:
        if item["aktiv"] == True:
            aktive.append(item["name"])
            
    return aktive

print(finde_aktive_produkte(webshop_produkte))

produkte = [
    {"name": "Tastatur", "preis": 50.0, "kategorie": "Hardware"},
    {"name": "Maus", "preis": 25.0, "kategorie": "Hardware"},
    {"name": "Office Lizenz", "preis": 100.0, "kategorie": "Software"}
]

def inflations_update(produkt_liste):

    for item in produkt_liste:
        if item["kategorie"] == "Hardware":
            item["preis"] = item["preis"] * 1.1
    
    return produkt_liste

print(inflations_update(produkte))