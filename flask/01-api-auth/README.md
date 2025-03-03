
# Correr los contenedores con docker compose
docker-compose up -d
docker-compose down

# Construir la imagen para luego usar
docker build -t flask-auth-api .

# Ejecutar tests
pytest tests/test_auth.py -v

# Instalar requerimientos
pip install -r requirements.txt

# Correr la App
python run.py

# Activar entorno virtual
venv\Scripts\activate