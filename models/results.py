from typing import Generic, TypeVar, Union

__all__ = ("Result")

from models.option import Option

T = TypeVar("T")
E = TypeVar("E")

def ok(result: "Result[T, E]") -> T:
    """
    Extract the success value from a result if it exists

    Args:
        result: The result to extract from

    Returns:
        The ok value

    Raises:
        ValueError if the result contains an error value
    """
    if result.is_ok():
        return result._value  # noqa
    raise ValueError("Called Ok on Err value")

def err(result: "Result[T, E]") -> E:
    """
    Extract the error value from a result if it exists

    Args:
        result: The result to extract from

    Returns:
        The err value

    Raises:
        ValueError if the result contains an ok value
    """
    if result.is_ok():
        raise ValueError("Called Err on Ok value")
    return result._value  # noqa

class Result(Generic[T, E]):
    """
    A result type that represents either a success value of Type T or an error value of Type E.
    This offers a nice pattern for handling errors without exceptions

    Type Parameters:
        T: The type of success value
        E: The type of error value

    Example
    ```
    def divide(a: float, b: float) -> Result[float, str]:
        if a == 0:
            return Result.err("Division by zero")
        return Result.ok(a/b)
    ```
    """

    _value: Union[T, E]
    _is_ok: bool

    def __init__(self, value: Union[T, E], is_ok: bool = False):
        self._value = value
        self._is_ok = is_ok

    def __consume__(self):
        """
        Called to consume/clear the value.
        Called after converting to Option to prevent reuse
        """
        self._value = None
        self._is_ok = False

    @classmethod
    def ok(cls, value: T) -> "Result[T, E]":
        """
        Create an instance representing a success

        Args:
            value: The value to store

        Returns:
            A result instance containing the success value
        """
        return cls(value, True)

    @classmethod
    def err(cls, error: E) -> "Result[T, E]":
        """
        Create an instance representing an error.

        Args:
            error: The error value to store

        Returns:
            A result instance containing the error value
        """
        return cls(error, False)

    def is_ok(self) -> bool:
        """Check if the Result contains a success value"""
        return self._is_ok

    def is_err(self) -> bool:
        """Check if the Result contains an error value"""
        return not self._is_ok

    def unwrap(self) -> T:
        """
        Get the contained success value

        Returns:
            The contained success value

        Raises:
            ValueError: If the result contains an error value
        """
        if self._is_ok:
            return self._value
        raise ValueError(f"Called unwrap on Err value: {self._value}")

    @property
    def err_to_option(self) -> Option[E]:
        """
        Converts from Result <T, E> to Option<E>, and discarding the success value if any.
        Consumes self.

        Returns:
            An Option containing the error if any
        """
        if self._is_ok:
            self.__consume__()
        return Option(self._value)

    @property
    def ok_to_option(self) -> Option[T]:
        """
        Converts from Result <T, E> to Option<T>, and discarding the error value if any.
        Consumes self.

        Returns:
            An Option containing the success value if any
        """
        if not self._is_ok:
            self.__consume__()
        return Option(self._value)
