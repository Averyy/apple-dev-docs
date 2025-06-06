# init(location:)

**Framework**: Xctest  
**Kind**: init

Initializes a new instance with a call stack from the executing thread and a provided source code location.

## Declaration

```swift
convenience init(location: XCTSourceCodeLocation?)
```

#### Discussion

The system derives the call stack from `NSThread.callStackReturnAddresses.`

## Parameters

- `location`: A representation of a location in source code.

## See Also

- [init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstack:location:).md)
  Initializes a new instance with a provided call stack and source code location.
- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstackaddresses:location:).md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init()](xctsourcecodecontext/init.md)
  Initializes a new instance with a call stack from the executing thread and no location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init(location:))*