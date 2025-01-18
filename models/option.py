from typing import Generic, TypeVar, Optional, Callable

__all__ = "Option"

T = TypeVar('T')
U = TypeVar('U')

class Option(Generic[T]):
    """
    An option type that represents either a value of Type T or None.
    This provides a more explicit way to handle optional values than using None directly.

    Type Parameters:
        T: The type of the contained value

    Example:
    ```
    def get_user_by_id(id: int) -> Option[User]:
        user = database.query(id)
        if user:
            return Option.some(user)
        return Option.none()
    ```
    """
    def __init__(self, value: Optional[T] = None):
        self._value = value
        self._is_some = value is not None

    @classmethod
    def some(cls, value: T) -> 'Option[T]':
        """
        Create an instance containing a value.

        Args:
            value: The value to store. Cannot be None.

        Returns:
            An option instance containing the value

        Raises:
            ValueError: If the provided value is None
        """
        if value is None:
            raise ValueError("Cannot have Some of None")
        return cls(value)

    @classmethod
    def none(cls) -> 'Option[T]':
        """
        Create an empty instance.

        Returns:
            An option instance containing no value
        """
        return cls()

    def is_some(self) -> bool:
        """Check if the Option contains a value"""
        return self._is_some

    def is_none(self) -> bool:
        """Check if the Option contains no value"""
        return not self._is_some

    def unwrap(self) -> T:
        """
        Get the contained value

        Returns:
            The contained value

        Raises:
            ValueError: If the option contains no value
        """
        if self._is_some:
            return self._value
        raise ValueError("Called unwrap on None value")