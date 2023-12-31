import azure.functions as func
import logging
from direct import eta

app = func.FunctionApp()
@app.route(route="req", auth_level=func.AuthLevel.ANONYMOUS)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # check if method is GET
    if req.method == "GET":
        # get the data from the query string
        route = req.params.get("route")
        departure = req.params.get("departure")

        # call eta function to get JSON update content to send as response to client
        response = eta(route, departure)

        # send response to client
        return func.HttpResponse(response, status_code=200)
    elif req.method == "POST":
        # get the data from the body
        route = req.get_json().get("route")
        departure = req.get_json().get("departure")

        # call eta function to get JSON update content to send as response to client
        response = eta(route, departure)

        # send response to client
        return func.HttpResponse(response, status_code=200)