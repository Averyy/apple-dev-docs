# XCTSourceCodeFrame

**Framework**: Xctest  
**Kind**: class

An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.

## Declaration

```swift
class XCTSourceCodeFrame
```

## Topics

### Initializers
- [init(address: UInt64, symbolInfo: XCTSourceCodeSymbolInfo?)](xctsourcecodeframe/init(address:symbolinfo:).md)
  Initializes an instance with a frame address and symbol information.
- [convenience init(address: UInt64)](xctsourcecodeframe/init(address:).md)
  Initializes an instance with a frame address.
### Frame Information
- [var address: UInt64](xctsourcecodeframe/address.md)
  An address that represents a specific frame in a call stack.
- [var symbolInfo: XCTSourceCodeSymbolInfo?](xctsourcecodeframe/symbolinfo.md)
  Symbolication information for the referenced frame.
- [var symbolicationError: (any Error)?](xctsourcecodeframe/symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](xctsourcecodeframe/symbolinfo.md)
  Attempts to get symbol information for the address.

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
- [class XCTSourceCodeContext](xctsourcecodecontext.md)
  An object that contains call stack and source code location details to provide context for a point of execution in a test.
- [class XCTSourceCodeLocation](xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe)*