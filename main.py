import uuid

import grpc
from flask import Flask, request
import messages_pb2 as pb
import messages_pb2_grpc as gpb
import logging

app = Flask(__name__)
app.secret_key = str(uuid.uuid4())
_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, filename='./logs/server.log', filemode='a+')



@app.route('/')
def hello():
    try:
        channel = grpc.insecure_channel('grpcserver:50051')
        stub = gpb.RequestHandlerStub(channel=channel)
        requestData = pb.RequestData(page_name=request.url, request_body=str(request.form.to_dict()), client_address=request.host)
        response = stub.HandleRequest(requestData)
        if response.status == pb.StatusEnum.RECEIVED:
            _logger.info('Received')
        elif response.status == pb.StatusEnum.RECORDED:
            _logger.info("Recorded")
        else:
            _logger.info("Message: %s.", response)
    except Exception as e:
        _logger.error("%s: %s", type(e).__name__, e)
    return "Message Received."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
