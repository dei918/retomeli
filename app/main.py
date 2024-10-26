from fastapi import FastAPI
import psutil
import subprocess
from pydantic import BaseModel

app = FastAPI()

class ScriptRequest(BaseModel):
    script_name: str

@app.get("/device_usage")
def get_device_usage(device: str = "/"):
    usage = psutil.disk_usage(device)
    return {
        "total": usage.total,
        "used": usage.used,
        "free": usage.free,
        "percent": usage.percent
    }

@app.get("/cpu_usage")
def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)  # intervalo de 1 segundo para calcular el porcentaje de uso
    return {"cpu_percent": cpu_percent}

@app.post("/run_script")
def run_script(request: ScriptRequest):
    try:
        result = subprocess.run([f"./app/scripts/{request.script_name}"], capture_output=True, text=True)
        return {"output": result.stdout, "error": result.stderr}
    except Exception as e:
        return {"error": str(e)}
