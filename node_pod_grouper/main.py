from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from node_pod_grouper.node_pod_grouper import NodePodGrouperService  # Corrected import

app = FastAPI()
service = NodePodGrouperService()

@app.get("/nodes")
async def get_nodes():
    """Endpoint to get a dictionary mapping node names to lists of pod details."""
    try:
        node_pod_map = service.get_nodes()
        return JSONResponse(content=jsonable_encoder(node_pod_map))
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/nodes/{node_name}")
async def get_node(node_name: str):
    """Endpoint to get a list of pod details running on the specified node."""
    try:
        pods = service.get_node(node_name)
        return JSONResponse(content=jsonable_encoder(pods))
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
