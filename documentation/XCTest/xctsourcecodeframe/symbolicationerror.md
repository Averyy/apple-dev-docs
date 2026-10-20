# symbolicationError

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

An optional error that describes a failed symbolication attempt.

## Declaration

```swift
var symbolicationError: (any Error)? { get }
```

```objc
@property (readonly, nullable) NSError * symbolicationError;
```

#### Discussion

The system doesn’t serialize this error when it encodes the frames.

## See Also

### Frame Information
- [var address: UInt64](./address.md)
  An address that represents a specific frame in a call stack.
- [var symbolInfo: XCTSourceCodeSymbolInfo?](./symbolinfo.md)
  Symbolication information for the referenced frame.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](./symbolinfo%28%29.md)
  Attempts to get symbol information for the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/symbolicationerror)*