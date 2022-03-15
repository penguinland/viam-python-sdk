import abc

from viam.proto.api.common import Pose
from viam.proto.api.component.arm import JointPositions

from ..component_base import ComponentBase


class Arm(ComponentBase):
    """
    Abstract representation of a physical Arm that
    exists in three-dimensional space

    If you override the init function,
    you must call the super init function.
    """

    @abc.abstractmethod
    async def get_end_position(self) -> Pose:
        """
        Get the current position of the arm

        Returns:
            Pose: Current position of the arm
        """
        ...

    @abc.abstractmethod
    async def move_to_position(self, pose: Pose):
        """
        Move the arm to the given absolute position

        Args:
            pose (Pose): The position to move the arm to
        """
        ...

    @abc.abstractmethod
    async def move_to_joint_positions(self, positions: JointPositions):
        """
        Move this arm's joints to the given positions

        Args:
            positions (JointPositions): The positions to move the joints to
        """
        ...

    @abc.abstractmethod
    async def get_joint_positions(self) -> JointPositions:
        """
        Get the current joint positions for this arm

        Returns:
            JointPositions: The current joint positions
        """
        ...
