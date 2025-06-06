# symbolicationError

**Framework**: Xctest  
**Kind**: property

An optional error that describes a failed symbolication attempt.

## Declaration

```swift
var symbolicationError: (any Error)? { get }
```

#### Discussion

The system doesn’t serialize this error when it encodes the frames.

## See Also

- [var address: UInt64](xctsourcecodeframe/address.md)
  An address that represents a specific frame in a call stack.
- [var symbolInfo: XCTSourceCodeSymbolInfo?](xctsourcecodeframe/symbolinfo.md)
  Symbolication information for the referenced frame.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](xctsourcecodeframe/symbolinfo.md)
  Attempts to get symbol information for the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/symbolicationerror)*