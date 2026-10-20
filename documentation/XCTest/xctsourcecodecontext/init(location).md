# init(location:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Initializes a new instance with a call stack from the executing thread and a provided source code location.

## Declaration

```swift
convenience init(location: XCTSourceCodeLocation?)
```

```objc
- (instancetype) initWithLocation:(XCTSourceCodeLocation *) location;
```

#### Discussion

The system derives the call stack from `NSThread.callStackReturnAddresses.`

## Parameters

- `location`: A representation of a location in source code.

## See Also

### Initializers
- [init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)](./init%28callstack,location%29.md)
  Initializes a new instance with a provided call stack and source code location.
- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](./init%28callstackaddresses,location%29.md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init()](./init%28%29.md)
  Initializes a new instance with a call stack from the executing thread and no location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init(location:))*