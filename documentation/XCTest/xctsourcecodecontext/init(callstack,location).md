# init(callStack:location:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a new instance with a provided call stack and source code location.

## Declaration

```swift
init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)
```

```objc
- (instancetype) initWithCallStack:(NSArray<XCTSourceCodeFrame *> *) callStack location:(XCTSourceCodeLocation *) location;
```

## Parameters

- `callStack`: An array of source code frames that describe the call stack.
- `location`: A representation of a location in source code.

## See Also

### Initializers
- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](./init%28callstackaddresses,location%29.md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init(location: XCTSourceCodeLocation?)](./init%28location%29.md)
  Initializes a new instance with a call stack from the executing thread and a provided source code location.
- [convenience init()](./init%28%29.md)
  Initializes a new instance with a call stack from the executing thread and no location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init(callstack:location:))*