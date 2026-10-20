# symbolInfo

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

Symbolication information for the referenced frame.

## Declaration

```swift
var symbolInfo: XCTSourceCodeSymbolInfo? { get }
```

```objc
@property (readonly, nullable) XCTSourceCodeSymbolInfo * symbolInfo;
```

## See Also

### Frame Information
- [var address: UInt64](./address.md)
  An address that represents a specific frame in a call stack.
- [var symbolicationError: (any Error)?](./symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](./symbolinfo%28%29.md)
  Attempts to get symbol information for the address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/symbolinfo)*