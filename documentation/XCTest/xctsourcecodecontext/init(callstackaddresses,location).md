# init(callStackAddresses:location:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a new instance with an array of call stack addresses and a source code location.

## Declaration

```swift
convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)
```

```objc
- (instancetype) initWithCallStackAddresses:(NSArray<NSNumber *> *) callStackAddresses location:(XCTSourceCodeLocation *) location;
```

## Discussion

The call stack addresses could be from `NSThread.callStackReturnAddresses`, `NSException.callStackReturnAddresses`, or another source.

## Parameters

- `callStackAddresses`: An array of call stack return addresses.
- `location`: A representation of a location in source code.

## See Also

### Initializers
- [init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)](./init%28callstack,location%29.md)
  Initializes a new instance with a provided call stack and source code location.
- [convenience init(location: XCTSourceCodeLocation?)](./init%28location%29.md)
  Initializes a new instance with a call stack from the executing thread and a provided source code location.
- [convenience init()](./init%28%29.md)
  Initializes a new instance with a call stack from the executing thread and no location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init(callstackaddresses:location:))*