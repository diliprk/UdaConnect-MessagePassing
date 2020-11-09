# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person.proto',
  package='lmjwtest',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0cperson.proto\x12\x08lmjwtest\"G\n\x08persontx\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x03 \x01(\t\"\x18\n\x04resp\x12\x10\n\x08respText\x18\x01 \x01(\t2D\n\rPersonService\x12\x33\n\x0bstorePerson\x12\x12.lmjwtest.persontx\x1a\x0e.lmjwtest.resp\"\x00\x62\x06proto3'
)




_PERSONTX = _descriptor.Descriptor(
  name='persontx',
  full_name='lmjwtest.persontx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='lmjwtest.persontx.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='lmjwtest.persontx.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='company_name', full_name='lmjwtest.persontx.company_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=97,
)


_RESP = _descriptor.Descriptor(
  name='resp',
  full_name='lmjwtest.resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='respText', full_name='lmjwtest.resp.respText', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['persontx'] = _PERSONTX
DESCRIPTOR.message_types_by_name['resp'] = _RESP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

persontx = _reflection.GeneratedProtocolMessageType('persontx', (_message.Message,), {
  'DESCRIPTOR' : _PERSONTX,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:lmjwtest.persontx)
  })
_sym_db.RegisterMessage(persontx)

resp = _reflection.GeneratedProtocolMessageType('resp', (_message.Message,), {
  'DESCRIPTOR' : _RESP,
  '__module__' : 'person_pb2'
  # @@protoc_insertion_point(class_scope:lmjwtest.resp)
  })
_sym_db.RegisterMessage(resp)



_PERSONSERVICE = _descriptor.ServiceDescriptor(
  name='PersonService',
  full_name='lmjwtest.PersonService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=125,
  serialized_end=193,
  methods=[
  _descriptor.MethodDescriptor(
    name='storePerson',
    full_name='lmjwtest.PersonService.storePerson',
    index=0,
    containing_service=None,
    input_type=_PERSONTX,
    output_type=_RESP,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONSERVICE)

DESCRIPTOR.services_by_name['PersonService'] = _PERSONSERVICE

# @@protoc_insertion_point(module_scope)