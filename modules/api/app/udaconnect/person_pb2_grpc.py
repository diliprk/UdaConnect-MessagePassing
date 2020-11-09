# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import person_pb2 as person__pb2


class PersonServiceStub(object):
    """service, encode a plain text 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.storePerson = channel.unary_unary(
                '/lmjwtest.PersonService/storePerson',
                request_serializer=person__pb2.persontx.SerializeToString,
                response_deserializer=person__pb2.resp.FromString,
                )


class PersonServiceServicer(object):
    """service, encode a plain text 
    """

    def storePerson(self, request, context):
        """request a service of encode
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'storePerson': grpc.unary_unary_rpc_method_handler(
                    servicer.storePerson,
                    request_deserializer=person__pb2.persontx.FromString,
                    response_serializer=person__pb2.resp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'lmjwtest.PersonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersonService(object):
    """service, encode a plain text 
    """

    @staticmethod
    def storePerson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/lmjwtest.PersonService/storePerson',
            person__pb2.persontx.SerializeToString,
            person__pb2.resp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
