from typing import Any

from lagom.exceptions import InjectableMarkerConsumed


class Injectable:
    """
    This class is looked for when analysing function signatures for arguments to
    injected
    """

    def __bool__(self):
        """
        If this is used in an if statement it should be falsy as it indicates the dependency
        has not been injected.
        :return:
        """
        return False

    def __getattribute__(self, item):
        raise InjectableMarkerConsumed()


# singleton object used to indicate that an argument should be injected
injectable: Any = Injectable()
