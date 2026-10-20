# address

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

An address that represents a specific frame in a call stack.

## Declaration

```swift
var address: UInt64 { get }
```

```objc
@property (readonly) uint64_t address;
```

## See Also

### Frame Information
- [var symbolInfo: XCTSourceCodeSymbolInfo?](./symbolinfo.md)
  Symbolication information for the referenced frame.
- [var symbolicationError: (any Error)?](./symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](./symbolinfo%28%29.md)
  Attempts to get symbol information for the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/address)*