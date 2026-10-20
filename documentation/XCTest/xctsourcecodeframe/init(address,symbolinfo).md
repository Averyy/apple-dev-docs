# init(address:symbolInfo:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes an instance with a frame address and symbol information.

## Declaration

```swift
init(address: UInt64, symbolInfo: XCTSourceCodeSymbolInfo?)
```

```objc
- (instancetype) initWithAddress:(uint64_t) address symbolInfo:(XCTSourceCodeSymbolInfo *) symbolInfo;
```

## Parameters

- `address`: An address that represents a specific frame in a call stack.
- `symbolInfo`: Symbolication information for the referenced frame.

## See Also

### Initializers
- [convenience init(address: UInt64)](./init%28address%29.md)
  Initializes an instance with a frame address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe/init(address:symbolinfo:))*