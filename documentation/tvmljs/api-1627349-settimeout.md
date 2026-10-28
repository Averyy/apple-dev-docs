# setTimeout

**Framework**: TVMLKit JS  
**Kind**: func  
**Role**: Function

Executes a given function after a set amount of time.

**Availability**:
- tvOS 9.0+

## Declaration

```
String setTimeout(
    in Function func, 
    in Integer time
);
```

## Return Value

Returns a string containing an identifier for the timeout just set.

## Discussion

Pass the identifier created by this function to the [`clearTimeout`](./api-1627416-cleartimeout.md) function to stop the designated function from executing.

## Parameters

- `func`: The function to be executed.
- `time`: An integer value that defines, in milliseconds, how long until the function is executed.

## See Also

### Automating Function Timing
- [setInterval](./api-1627337-setinterval.md)
  Repeatedly executes a given function at the given time interval.
- [clearInterval](./api-1627411-clearinterval.md)
  Stops the function associated with the identifier from repeating.
- [clearTimeout](./api-1627416-cleartimeout.md)
  Stops the function associated with the identifier from executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627349-settimeout)*