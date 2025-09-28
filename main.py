import json
from fastapi import FastAPI

# Initialisiere die FastAPI-App
app = FastAPI()

# Lade die JSON-Daten aus der Datei, wenn die Anwendung startet
# Dies geschieht nur einmal, was effizienter ist als bei jeder Anfrage
try:
    with open("data.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
except FileNotFoundError:
    json_data = {"error": "data.json not found"}


@app.get("/")
def read_root():
    """
    Ein einfacher Willkommens-Endpunkt.
    """
    return {"message": "Willkommen! Gehe zu /data, um die JSON-Daten zu sehen."}


@app.get("/data")
def get_json_data():
    """
    Dieser Endpunkt gibt den Inhalt der geladenen JSON-Datei zurück.
    """
    return json_data
