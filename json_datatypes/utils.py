"""General helper functions."""


from typing import (
    Any,
    DefaultDict,
    Hashable
)

class KeyDependentDefaultDict(DefaultDict):
    """Subclass of defaultdict that passes the missing key to the default_factory.

    Attributes:
        default_factory: A function that is called when getting a missing
            key from the dictionary. The function will be called with the
            value of the key as it's only argument. The return of the function
            will be returned as the value of the key.

    """

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the object.

        Arguments:
            args: If present, the first value will be used as the
                default_factory. Remaining arguments are passed to the parent
                constructor.
            kwargs: Keyword arguments are passed to the parent constructor.

        """
        args = list(args)
        default_factory = args.pop(0) if args else None

        super(KeyDependentDefaultDict, self).__init__(None, *args, **kwargs)

        self.default_factory = default_factory

    def __missing__(self, key: Hashable) -> Any:
        """Called for key values that are missing from the dictionary.

        If default_factory is not None, it is called with the key as argument.

        """
        if self.default_factory is not None:
            return self.default_factory(key)
        else:
            raise KeyError(key)
