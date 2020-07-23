# Pour fusionner le .env avec les variables d'environnement

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
