# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\"\x8f\x01\n\x0bRequestData\x12\x16\n\tpage_name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0e\x63lient_address\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0crequest_body\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0c\n\n_page_nameB\x11\n\x0f_client_addressB\x0f\n\r_request_body\"\x8c\x01\n\x0cResponseBody\x12(\n\x06status\x18\x01 \x01(\x0e\x32\x18.ResponseBody.StatusEnum\"R\n\nStatusEnum\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08RECEIVED\x10\x01\x12\x0c\n\x08RECORDED\x10\x02\x12\x19\n\x15\x45RROR_WHILE_RECORDING\x10\x03\x32@\n\x0eRequestHandler\x12.\n\rHandleRequest\x12\x0c.RequestData\x1a\r.ResponseBody\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_REQUESTDATA']._serialized_start=19
  _globals['_REQUESTDATA']._serialized_end=162
  _globals['_RESPONSEBODY']._serialized_start=165
  _globals['_RESPONSEBODY']._serialized_end=305
  _globals['_RESPONSEBODY_STATUSENUM']._serialized_start=223
  _globals['_RESPONSEBODY_STATUSENUM']._serialized_end=305
  _globals['_REQUESTHANDLER']._serialized_start=307
  _globals['_REQUESTHANDLER']._serialized_end=371
# @@protoc_insertion_point(module_scope)
