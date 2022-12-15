import dotenv
import os
import pytz

dotenv.load_dotenv(dotenv.find_dotenv())
client = os.getenv('mongoClient')
Pw = os.getenv('mongoPW')

#   PYTZ
tz_brazil = pytz.timezone('America/Sao_Paulo')


#   MONGODB
mongo = f"mongodb"


#   GUILD


#   CORES
roxo = 0x690FC3
vermelho = 0xff0000


#   CARGOS AUTOMATICOS/STAFF -----


#   CARGOS PING ----------------
#   PING DIARIO


#   PING SQUAD


#   PING ALERTAS


#   CARGOS PERSONALIZADOS -----


#   CARGOS PADRÃO -----


#   SALAS DE TEXTO ================


