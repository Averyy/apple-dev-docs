# address

**Framework**: Xctest  
**Kind**: property

An address that represents a specific frame in a call stack.

## Declaration

```swift
var address: UInt64 { get }
```

## See Also

- [var symbolInfo: XCTSourceCodeSymbolInfo?](xctsourcecodeframe/symbolinfo.md)
  Symbolication information for the referenced frame.
- [var symbolicationError: (any Error)?](xctsourcecodeframe/symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](xctsourcecodeframe/symbolinfo.md)
  Attempts to get symbol information for the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/address)*