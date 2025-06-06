# clearTimeout

**Framework**: TVMLKit JS  
**Kind**: func

Stops the function associated with the identifier from executing.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
void clearTimeout(
    in String timeoutID
);
```

#### Discussion

This function stops the function associated with the identifier created by the [`setTimeout`](1627349-settimeout.md) function from executing.

## Parameters

- `timeoutID`: A string identifying the timeout to clear.

## See Also

- [setInterval](1627337-setinterval.md)
  Repeatedly executes a given function at the given time interval.
- [clearInterval](1627411-clearinterval.md)
  Stops the function associated with the identifier from repeating.
- [setTimeout](1627349-settimeout.md)
  Executes a given function after a set amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627416-cleartimeout)*