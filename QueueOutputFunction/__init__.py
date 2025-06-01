import azure.functions as func
import json

def main(req: func.HttpRequest, outputQueueItem: func.Out[str]) -> func.HttpResponse:
    name = req.params.get('name')
    if not name:
        return func.HttpResponse("Please pass a name in the query string", status_code=400)

    message = json.dumps({ "name": name })
    outputQueueItem.set(message)
    return func.HttpResponse(f"Queued message for {name}")
