# XCTSourceCodeContext

**Framework**: Xctest  
**Kind**: class

An object that contains call stack and source code location details to provide context for a point of execution in a test.

## Declaration

```swift
class XCTSourceCodeContext
```

## Topics

### Initializers
- [init(callStack: [XCTSourceCodeFrame], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstack:location:).md)
  Initializes a new instance with a provided call stack and source code location.
- [convenience init(callStackAddresses: [NSNumber], location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(callstackaddresses:location:).md)
  Initializes a new instance with an array of call stack addresses and a source code location.
- [convenience init(location: XCTSourceCodeLocation?)](xctsourcecodecontext/init(location:).md)
  Initializes a new instance with a call stack from the executing thread and a provided source code location.
- [convenience init()](xctsourcecodecontext/init.md)
  Initializes a new instance with a call stack from the executing thread and no location.
### Context Information
- [var callStack: [XCTSourceCodeFrame]](xctsourcecodecontext/callstack.md)
  An array of source code frames that describes the call stack when a test issue occurs.
- [var location: XCTSourceCodeLocation?](xctsourcecodecontext/location.md)
  A representation of a location in source code where a test issue occurred.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [struct XCTIssue](xctissue-swift.struct.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTIssueReference](xctissuereference.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTMutableIssue](xctmutableissue.md)
  A mutable object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTSourceCodeFrame](xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeLocation](xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodecontext)*