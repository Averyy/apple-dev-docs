# symbolInfo()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Attempts to get symbol information for the address.

## Declaration

```swift
func symbolInfo() throws -> XCTSourceCodeSymbolInfo
```

```objc
- (XCTSourceCodeSymbolInfo *) symbolInfoWithError:(NSError **) outError;
```

#### Return Value

Symbol information for the address.

#### Discussion

This method can fail if required symbol data is not available. The system makes only one attempt to retrieve the symbol information. If that attempt fails, the system stores the error and returns it for future requests.

## See Also

### Frame Information
- [var address: UInt64](./address.md)
  An address that represents a specific frame in a call stack.
- [var symbolInfo: XCTSourceCodeSymbolInfo?](./symbolinfo.md)
  Symbolication information for the referenced frame.
- [var symbolicationError: (any Error)?](./symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/symbolinfo())*