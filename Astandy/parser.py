from typing import Any, Sequence

from Astandy.errors import AstandyRPCException
from Astandy.schemes.messages_pb2 import ClientMsg, BinaryValue, Response, ServerMsg

class Parser:
    @staticmethod
    def new_msg(
        uuid: str,
        code: int,
        payload: bytes,
        service: str = "",
        method: str = "",
    ):
        msg = ClientMsg(id=uuid, code=code)
        if code == 0:
            msg.cls = service
            msg.func = method

        msg.data.append(BinaryValue(one=payload))

        return msg.SerializeToString()
    
    @staticmethod
    def parse_response(request: bytes) -> ServerMsg:
        msg = ServerMsg()
        msg.ParseFromString(request)

        return msg

    @staticmethod
    def raise_for_exception(response: Response) -> None:
        if response.exception.code:
            raise AstandyRPCException(response.exception)

    @staticmethod
    def parse_rpc_response(response: Response, response_cls: type) -> Any:
        Parser.raise_for_exception(response)
        payload = response.data[0].one if response.data else b""
        message = response_cls()
        message.ParseFromString(payload)
        return message

    @staticmethod
    def parse_empty_rpc_response(response: Response) -> None:
        Parser.raise_for_exception(response)
        return None

    @staticmethod
    def serialize_primitive_payload(value: Any, type_name: str) -> bytes:
        from Astandy.generated.protos import rpc_message_pb2

        if type_name == "string":
            return rpc_message_pb2.String(value=value).SerializeToString()
        if type_name == "byte[]":
            return rpc_message_pb2.Byte(value=bytes(value)).SerializeToString()
        if type_name == "int":
            return rpc_message_pb2.Integer(value=value).SerializeToString()
        if type_name == "long":
            return rpc_message_pb2.Long(value=value).SerializeToString()
        if type_name == "float":
            return rpc_message_pb2.Float(value=value).SerializeToString()
        if type_name == "double":
            return rpc_message_pb2.Double(value=value).SerializeToString()
        if type_name == "bool":
            return rpc_message_pb2.Boolean(value=value).SerializeToString()
        raise TypeError(f"unsupported primitive RPC parameter type: {type_name}")

    @staticmethod
    def serialize_primitive_request(params: list[tuple[str, Any]]) -> list[bytes]:
        return [
            Parser.serialize_primitive_payload(value, type_name)
            for type_name, value in params
        ]
