# init(callStack:location:)

**Framework**: XCTest  
**Kind**: init

Initializes a new instance with a provided call stack and source code location.

## Declaration

```swift
init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)
```

## Parameters

- `callStack`: An array of source code frames that describe the call stack.
- `location`: A representation of a location in source code.

## See Also

- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstackaddresses:location:).md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init(location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(location:).md)
  Initializes a new instance with a call stack from the executing thread and a provided source code location.
- [convenience init()](xctsourcecodecontext/init.md)
  Initializes a new instance with a call stack from the executing thread and no location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext/init(callstack:location:))*