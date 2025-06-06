# clearInterval

**Framework**: TVMLKit JS  
**Kind**: func

Stops the function associated with the identifier from repeating.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void clearInterval(
    in String intervalID
);
```

#### Discussion

This function stops the function associated with the identifier created by the [`setInterval`](1627337-setinterval.md) function from executing.

## Parameters

- `intervalID`: A string identifying the interval to clear.

## See Also

- [setInterval](1627337-setinterval.md)
  Repeatedly executes a given function at the given time interval.
- [setTimeout](1627349-settimeout.md)
  Executes a given function after a set amount of time.
- [clearTimeout](1627416-cleartimeout.md)
  Stops the function associated with the identifier from executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627411-clearinterval)*