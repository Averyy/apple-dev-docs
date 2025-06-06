# init()

**Framework**: Xctest  
**Kind**: init

Initializes a new instance with a call stack from the executing thread and no location.

## Declaration

```swift
convenience init()
```

#### Discussion

The system derives the call stack from `NSThread.callStackReturnAddresses.`

## See Also

- [init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstack:location:).md)
  Initializes a new instance with a provided call stack and source code location.
- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstackaddresses:location:).md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init(location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(location:).md)
  Initializes a new instance with a call stack from the executing thread and a provided source code location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init())*