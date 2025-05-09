
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
import pandas as pd
from pymongo import MongoClient
from pymongo import UpdateOne
import os
from datetime import datetime
from dotenv import load_dotenv
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

load_dotenv()
MONGODB_URI = os.getenv("MONGODB_URI")

client = MongoClient(MONGODB_URI, server_api=ServerApi('1'), tlsCAFile=certifi.where())

# test conection
try:
    client.admin.command('ping')
    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    logging.error("Invalid connection")
    raise e

path_csv = os.path.join(os.path.dirname(__file__), '../data/dados_veiculos.csv')
df = pd.read_csv(path_csv)

db = client['data-engineer']
col_vehicles = db['vehicles']
col_owners = db['owners']

df = df.fillna('')
vehicles_bulk = []
owners_bulk = []

for _, row in df.iterrows():
    vehicle_doc = {
        "brand": row["Marca do Veículo"],
        "model": row["Modelo do Veículo"],
        "manufacture_year": int(row["Ano de Fabricação"]),
        "mileage": float(row["Quilometragem"]),
        "fuel_type": row["Tipo de Combustível"],
        "price": float(row["Valor do Veículo"]),
        "has_fines": row["Tem Multas?"] == "Sim",
        "has_insurance": row["Tem Seguro?"] == "Sim",
        "color": row["Cor do Veículo"],
        "transmission": row["Tipo de Câmbio"],
        "doors": int(row["Número de Portas"]),
        "safety": {
            "airbag": row["Tem Airbag?"] == "Sim",
            "abs": row["Tem ABS?"] == "Sim"
        },
        "last_service_date": datetime.strptime(row["Data da Última Revisão"], "%d/%m/%Y"),
        "owner_cpf": row["CPF"]
    }

    vehicles_bulk.append(vehicle_doc)

result = col_vehicles.insert_many(vehicles_bulk)
logging.info(f"Inserted {len(result.inserted_ids)} vehicles.")

for vehicle_doc, vehicle_id in zip(vehicles_bulk, result.inserted_ids):
    cpf = vehicle_doc["owner_cpf"]
    owners_bulk.append(
        UpdateOne(
            {"_id": cpf},
            {"$addToSet": {"vehicles": {"vehicle_id": vehicle_id}}},
            upsert=True
        )
    )

if owners_bulk:
    owner_result = col_owners.bulk_write(owners_bulk)
    logging.info(f"Modified {owner_result.modified_count} owners.")
else:
    logging.info("No owners to modify.")