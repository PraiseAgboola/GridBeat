from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/status")
async def read_status():
    return {"status": "Grid is operating normally"}

@app.get("/monitor/{area}")
async def monitor_area(area: str):
    # Here you would implement the monitoring logic for the specific area
    return {"message": f"Monitoring grid in {area}", "status": "Operational"}

@app.post("/report/{area}")
async def report_issue(area: str, issue: str):
    # Logic to handle reported issues
    if not issue:
        raise HTTPException(status_code=400, detail="No issue reported")
    return {"message": f"Issue reported in {area}: {issue}", "status": "Under investigation"}
