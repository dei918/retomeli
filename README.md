Subir deployment:

docker-compose up --build -d

Bajar deployment:

docker-compose down

Consultar uso de disco

curl -X 'GET' 'http://localhost:8000/device_usage?device=/' -H 'accept: application/json'

Consultar uso de cpu

curl -X 'GET' 'http://localhost:8000/cpu_usage' -H 'accept: application/json'

Ejecutar script

curl -X 'POST' 'http://localhost:8000/run_script' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"script_name": "script.sh"}'
