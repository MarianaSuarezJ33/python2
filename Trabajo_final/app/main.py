from fastapi import FastAPI
from . import routes

app = FastAPI()

# Monta las rutas definidas en routes.py
app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
