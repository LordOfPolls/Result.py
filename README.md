# Result.py

> Bringing the Rust result type to Python, whether you like it or not 

## What is `Result`
`Result` is a way to represent a value that can either be a success (Ok) or an error (Err). 
This makes error handling explicit and clean. 

## Why would I use this instead of exceptions? 
Because sometimes you want your errors to be obvious. 
Exceptions are landmines waiting to blow up your program at runtime. 
With `Result`, errors are an actual part of your program, rather than a secondary execution path you don't control. 

You might want this if: 
- You actually want to handle errors, rather than hiding them behind try-except
- You enjoy the peace of mind of knowing exactly where things could go wrong
- You're a rust developer being forced to program in Python 
- Your code has more try-except blocks than actual logic

Still not convinced? 
Think of it as bringing some typing goodness to your error handling. 

## Examples
```py
def divide(a: float, b: float) -> Result[float, str]:
    if a == 0:
        return Result.err("Division by zero")
    return Result.ok(a/b)

if __name__ == "__main__":
    # Success case
    result = divide(10, 2)
    if result.is_ok():
        print(f"10 / 2 = {result.unwrap()}")  # Prints: 10 / 2 = 5.0

    # Error case
    result = divide(10, 0)
    if result.is_err():
        print("Error: Cannot divide by zero")  # Prints: Error: Cannot divide by zero
```

## FAQ

#### Isn't this just overengineering?
Yes. *Typed* overengineering

#### Can't I just use try-except?
You could also write assembly, but here we are. 

#### Is this production ready?
Ask your team lead. I think yes, but I'm not them. 

## Installation
-- placeholder --


## Coming soon
- An actual package that can be installed through pip
    - It's on my todo once im done being tongue in cheek in this readme

## License
MIT... as it should be.

