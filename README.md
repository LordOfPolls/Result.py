# result-oxide

> Bringing Rust's Result and Option types to Python, whether you like it or not 

## What are `Result` and `Option`?
`Result` is a way to represent a value that can either be a success (Ok) or an error (Err).
This makes error handling explicit and clean.

`Option` is a way to represent a value that might not exist (Some or None).
Think of it as a more explicit way to handle nullable values.

> "I call it my billion-dollar mistake. It was the invention of the null reference in 1965."  
> — [Tony Hoare, inventor of null references](https://en.wikipedia.org/wiki/Tony_Hoare)

## Why would I use this instead of exceptions and None? 
Because sometimes you want your errors and optional values to be obvious.
Exceptions are landmines waiting to blow up your program at runtime.
Unexpected None values are null pointer exceptions waiting to happen (and apparently cost the industry a billion dollars).

With `Result`, errors are an actual part of your program, rather than a secondary execution path you don't control.
With `Option`, null checks become explicit rather than an afterthought.

You might want this if: 
- You actually want to handle errors, rather than hiding them behind try-except
- You're tired of "AttributeError: NoneType has no attribute 'x'"
- You enjoy the peace of mind of knowing exactly where things could go wrong
- You're a rust developer being forced to program in Python 
- Your code has more try-except blocks than actual logic
- You've ever written `if x is not None` more than twice in a function
- You want to avoid contributing to the next billion dollars of null reference damage

Still not convinced? 
Think of it as bringing some typing goodness to your error and null handling. 

## Examples
```py
def divide(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return Result.err("Division by zero")
    return Result.ok(a/b)

if __name__ == "__main__":
    success_result = divide(8, 4)
    if success_result.is_ok():
        value = ok(success_result)  
        print(f"8 / 4 = {value}")
    else:
        error_msg = err(error_result)
        print(f"Error: {error_msg}") 
```

```py
@dataclass
class User:
    id: int
    name: str

def get_user(user_id: int, users: Dict[int, User]) -> Option[User]:
    """Example of returning an Option type"""
    if user_id in users:
        return Option.some(users[user_id])
    return Option.none()

if __name__ == "__main__":
    maybe_bob = get_user(456, users)
    if maybe_bob.is_some():
        user = some(maybe_bob) 
        print(f"Found user: {user.name}")  
    else:
        print("User not found")  
```


## FAQ

#### Isn't this just overengineering? 
Yes. _Typed_ overengineering

#### Can't I just use try-except / None checks?
You could also write assembly, but here you are. 

#### Is this production ready? 
Ask your team lead. I think yes, but I'm not them. 

## Installation
-- placeholder --

## License
MIT, as it should be