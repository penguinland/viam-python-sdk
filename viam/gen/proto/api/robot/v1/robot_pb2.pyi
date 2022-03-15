"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.struct_pb2
import typing
import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ComponentConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    PARENT_FIELD_NUMBER: builtins.int
    POSE_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    type: typing.Text = ...
    parent: typing.Text = ...

    @property
    def pose(self) -> global___Pose:
        ...

    def __init__(self, *, name: typing.Text=..., type: typing.Text=..., parent: typing.Text=..., pose: typing.Optional[global___Pose]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['pose', b'pose']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name', 'parent', b'parent', 'pose', b'pose', 'type', b'type']) -> None:
        ...
global___ComponentConfig = ComponentConfig

class ConfigRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___ConfigRequest = ConfigRequest

class ConfigResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    COMPONENTS_FIELD_NUMBER: builtins.int

    @property
    def components(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ComponentConfig]:
        ...

    def __init__(self, *, components: typing.Optional[typing.Iterable[global___ComponentConfig]]=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['components', b'components']) -> None:
        ...
global___ConfigResponse = ConfigResponse

class DoActionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___DoActionRequest = DoActionRequest

class DoActionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...

    def __init__(self) -> None:
        ...
global___DoActionResponse = DoActionResponse

class Pose(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    X_FIELD_NUMBER: builtins.int
    Y_FIELD_NUMBER: builtins.int
    Z_FIELD_NUMBER: builtins.int
    O_X_FIELD_NUMBER: builtins.int
    O_Y_FIELD_NUMBER: builtins.int
    O_Z_FIELD_NUMBER: builtins.int
    THETA_FIELD_NUMBER: builtins.int
    x: builtins.float = ...
    'millimeters of the end effector from the base'
    y: builtins.float = ...
    z: builtins.float = ...
    o_x: builtins.float = ...
    'ox, oy, oz, theta represents an orientation vector\n    Structured similarly to an angle axis, an orientation vector works differently. Rather than representing an orientation\n    with an arbitrary axis and a rotation around it from an origin, an orientation vector represents orientation\n    such that the ox/oy/oz components represent the point on the cartesian unit sphere at which your end effector is pointing\n    from the origin, and that unit vector forms an axis around which theta rotates. This means that incrementing/decrementing\n    theta will perform an in-line rotation of the end effector.\n    Theta is defined as rotation between two planes: the plane defined by the origin, the point (0,0,1), and the rx,ry,rz\n    point, and the plane defined by the origin, the rx,ry,rz point, and the new local Z axis. So if theta is kept at\n    zero as the north/south pole is circled, the Roll will correct itself to remain in-line.\n    Theta in pb.Pose should be degrees. It will be converted to radians in the internal OrientationVec.\n    '
    o_y: builtins.float = ...
    o_z: builtins.float = ...
    theta: builtins.float = ...

    def __init__(self, *, x: builtins.float=..., y: builtins.float=..., z: builtins.float=..., o_x: builtins.float=..., o_y: builtins.float=..., o_z: builtins.float=..., theta: builtins.float=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['o_x', b'o_x', 'o_y', b'o_y', 'o_z', b'o_z', 'theta', b'theta', 'x', b'x', 'y', b'y', 'z', b'z']) -> None:
        ...
global___Pose = Pose

class ExecuteFunctionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    'TODO(RDK-39): arguments'

    def __init__(self, *, name: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['name', b'name']) -> None:
        ...
global___ExecuteFunctionRequest = ExecuteFunctionRequest

class ExecuteFunctionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    STD_OUT_FIELD_NUMBER: builtins.int
    STD_ERR_FIELD_NUMBER: builtins.int

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        ...
    std_out: typing.Text = ...
    std_err: typing.Text = ...

    def __init__(self, *, results: typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]]=..., std_out: typing.Text=..., std_err: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['results', b'results', 'std_err', b'std_err', 'std_out', b'std_out']) -> None:
        ...
global___ExecuteFunctionResponse = ExecuteFunctionResponse

class ExecuteSourceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    SOURCE_FIELD_NUMBER: builtins.int
    ENGINE_FIELD_NUMBER: builtins.int
    source: typing.Text = ...
    engine: typing.Text = ...

    def __init__(self, *, source: typing.Text=..., engine: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['engine', b'engine', 'source', b'source']) -> None:
        ...
global___ExecuteSourceRequest = ExecuteSourceRequest

class ExecuteSourceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    STD_OUT_FIELD_NUMBER: builtins.int
    STD_ERR_FIELD_NUMBER: builtins.int

    @property
    def results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[google.protobuf.struct_pb2.Value]:
        ...
    std_out: typing.Text = ...
    std_err: typing.Text = ...

    def __init__(self, *, results: typing.Optional[typing.Iterable[google.protobuf.struct_pb2.Value]]=..., std_out: typing.Text=..., std_err: typing.Text=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['results', b'results', 'std_err', b'std_err', 'std_out', b'std_out']) -> None:
        ...
global___ExecuteSourceResponse = ExecuteSourceResponse

class ResourceRunCommandRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    COMMAND_NAME_FIELD_NUMBER: builtins.int
    ARGS_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    'Note(erd): okay in v1 because names are unique. v2 should be a VRN'
    command_name: typing.Text = ...

    @property
    def args(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, resource_name: typing.Text=..., command_name: typing.Text=..., args: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['args', b'args']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['args', b'args', 'command_name', b'command_name', 'resource_name', b'resource_name']) -> None:
        ...
global___ResourceRunCommandRequest = ResourceRunCommandRequest

class ResourceRunCommandResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULT_FIELD_NUMBER: builtins.int

    @property
    def result(self) -> google.protobuf.struct_pb2.Struct:
        ...

    def __init__(self, *, result: typing.Optional[google.protobuf.struct_pb2.Struct]=...) -> None:
        ...

    def HasField(self, field_name: typing_extensions.Literal['result', b'result']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['result', b'result']) -> None:
        ...
global___ResourceRunCommandResponse = ResourceRunCommandResponse