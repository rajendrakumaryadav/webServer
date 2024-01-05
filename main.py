import logging
import os
import uuid

import grpc
from flask import Flask, request

import messages_pb2 as pb
import messages_pb2_grpc as gpb

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())
# _logger = logging.getLogger(__name__)


@app.route('/')
def hello():
    try:
        hostname = os.getenv("GRPCHOST", "::")
        port = os.getenv("PORT", "50051")
        channel = grpc.insecure_channel(f'{hostname}:{port}')
        stub = gpb.RequestHandlerStub(channel=channel)
        requestData = pb.RequestData(page_name=request.url,
                                     request_body=str(request.form.to_dict()),
                                     client_address=request.host
                                     )
        response = stub.HandleRequest(requestData)
        if response.status == pb.StatusEnum.RECEIVED:
            logging.info('Received')
        elif response.status == pb.StatusEnum.RECORDED:
            logging.info("Recorded")
        else:
            logging.info("Message: %s.", response)
    except Exception as e:
        logging.error("%s: %s", type(e).__name__, e)
    return "Message Received."


if __name__ == '__main__':
    rest_port = os.getenv("RESTPORT", 5000)
    app.run(host='0.0.0.0', port=int(rest_port), debug=True)
