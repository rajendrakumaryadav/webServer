# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import messages_pb2 as messages__pb2


class RequestHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HandleRequest = channel.unary_unary(
                '/RequestHandler/HandleRequest',
                request_serializer=messages__pb2.RequestData.SerializeToString,
                response_deserializer=messages__pb2.ResponseBody.FromString,
                )


class RequestHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HandleRequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HandleRequest': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleRequest,
                    request_deserializer=messages__pb2.RequestData.FromString,
                    response_serializer=messages__pb2.ResponseBody.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RequestHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RequestHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HandleRequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RequestHandler/HandleRequest',
            messages__pb2.RequestData.SerializeToString,
            messages__pb2.ResponseBody.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
