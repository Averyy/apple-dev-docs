# setInterval

**Framework**: TVMLKit JS  
**Kind**: func

Repeatedly executes a given function at the given time interval.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
String setInterval(
    in Function func, 
    in Integer time
);
```

#### Return_value

Returns a string containing an identifier for the interval just set.

#### Discussion

Pass the identifier created by this function to the [`clearInterval`](1627411-clearinterval.md) function to stop the designated function from executing.

## Parameters

- `func`: The function to be executed.
- `time`: An integer value that defines, in milliseconds, how often the function is to repeat.

## See Also

- [clearInterval](1627411-clearinterval.md)
  Stops the function associated with the identifier from repeating.
- [setTimeout](1627349-settimeout.md)
  Executes a given function after a set amount of time.
- [clearTimeout](1627416-cleartimeout.md)
  Stops the function associated with the identifier from executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627337-setinterval)*