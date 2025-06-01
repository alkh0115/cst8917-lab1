import azure.functions as func
import logging
import json

def main(req: func.HttpRequest, outputSql: func.Out[func.SqlRow]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        title = req_body.get('title')
        is_complete = req_body.get('isComplete', False)

        row = func.SqlRow(title=title, isComplete=is_complete)

        outputSql.set(row)
        return func.HttpResponse(f"ToDo item '{title}' inserted.")
    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error inserting item.", status_code=500)
