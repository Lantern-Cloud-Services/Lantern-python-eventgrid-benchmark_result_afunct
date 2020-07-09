import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.warn('Python HTTP trigger function processed a request.')

    run = req.params.get('run')
    total = req.params.get('total')
    logging.info("##### RUN: " + run + ", TOTAL: " + total + " #####")


    return func.HttpResponse("complete")
