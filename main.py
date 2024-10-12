from fastapi import FastAPI, Request, HTTPException
from utils import is_valid_coordinate, fetch_distance_matrix

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.post("/route")
async def handle_routes(request: Request):
    # Step 1: Parse the incoming JSON body
    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON format")

    # Step 2: Extract the "coordinates" field
    coords = payload.get("coordinates")

    # Step 3: Validate that coordinates are provided and is a list
    if not coords or not isinstance(coords, list) or len(coords) < 2:
        raise HTTPException(
            status_code=400, detail="At least two coordinates are required"
        )

    # Step 4: Validate each coordinate
    for i, coord in enumerate(coords):
        if not is_valid_coordinate(coord):
            raise HTTPException(
                status_code=400, detail=f"Invalid coordinate at index {i}: {coord}"
            )

    matrix = fetch_distance_matrix(coordinates=coords)
    if(not matrix) :
        raise HTTPException(
            status_code=400, detail="Something went wrong"
        )

    return {
        "status": "ok",
        "response": matrix,
    }
