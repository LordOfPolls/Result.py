from typing import Generic, TypeVar, Union

__all__ = "Result"

T = TypeVar("T")
E = TypeVar("E")


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

    _value: T

    def __init__(self, value: Union[T, E], is_ok: bool = False):
        self._value = value
        self._is_ok = is_ok

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
