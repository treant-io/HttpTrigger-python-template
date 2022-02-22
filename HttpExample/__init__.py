import azure.functions as func
import json
def main(req: func.HttpRequest) -> func.HttpResponse:
    '''
    This function listens at endpoint "/api/HttpExample". Two ways to invoke it using "curl" command in bash:
    1. curl -d "HTTP Body" {your host}/api/HttpExample
    2. curl "{your host}/api/HttpExample?name=HTTP%20Query"
    '''

    if req.params.get('name'):
        response = "Hello, %s. Welcome to Treant!" % (req.params.get('name'))
    else:
        response = "Please pass a name on the query string or in the request body"

    return func.HttpResponse(body=json.dumps(response),
             status_code=200,
        )
    