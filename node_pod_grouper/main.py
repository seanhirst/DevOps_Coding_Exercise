from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from node_pod_grouper import NodePodGrouperService

app = FastAPI()

service = NodePodGrouperService()  # Instantiate the service class

@app.get("/nodes")
async def nodes():
    """Endpoint to get a dictionary mapping node names to lists of pods."""
    try:
        content = jsonable_encoder(service.get_nodes())
        return JSONResponse(content=content)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/nodes/{name}")
async def node(name: str):
    """Endpoint to get a list of pods running on the specified node."""
    try:
        content = jsonable_encoder(service.get_node(name))
        return JSONResponse(content=content)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
