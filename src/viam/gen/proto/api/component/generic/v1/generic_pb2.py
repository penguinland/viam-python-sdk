"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,proto/api/component/generic/v1/generic.proto\x12\x1eproto.api.component.generic.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto"Y\n\x10DoCommandRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x121\n\x07command\x18\x02 \x01(\x0b2\x17.google.protobuf.StructR\x07command"D\n\x11DoCommandResponse\x12/\n\x06result\x18\x01 \x01(\x0b2\x17.google.protobuf.StructR\x06result2\xbd\x01\n\x0eGenericService\x12\xaa\x01\n\tDoCommand\x120.proto.api.component.generic.v1.DoCommandRequest\x1a1.proto.api.component.generic.v1.DoCommandResponse"8\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/generic/{name}/do_commandB]\n+com.viam.rdk.proto.api.component.generic.v1Z.go.viam.com/rdk/proto/api/component/generic/v1b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.api.component.generic.v1.generic_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n+com.viam.rdk.proto.api.component.generic.v1Z.go.viam.com/rdk/proto/api/component/generic/v1'
    _GENERICSERVICE.methods_by_name['DoCommand']._options = None
    _GENERICSERVICE.methods_by_name['DoCommand']._serialized_options = b'\x82\xd3\xe4\x93\x022"0/viam/api/v1/component/generic/{name}/do_command'
    _DOCOMMANDREQUEST._serialized_start = 140
    _DOCOMMANDREQUEST._serialized_end = 229
    _DOCOMMANDRESPONSE._serialized_start = 231
    _DOCOMMANDRESPONSE._serialized_end = 299
    _GENERICSERVICE._serialized_start = 302
    _GENERICSERVICE._serialized_end = 491