from fastapi import FastAPI

app = FastAPI()

@app.get('/appcheck', status_code=200)
async def appcheck():
    return 'HealthApp ready to go'
