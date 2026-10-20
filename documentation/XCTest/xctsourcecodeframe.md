# XCTSourceCodeFrame

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.

## Declaration

```swift
class XCTSourceCodeFrame
```

```objc
@interface XCTSourceCodeFrame : NSObject
```

## Topics

### Initializers
- [init(address: UInt64, symbolInfo: XCTSourceCodeSymbolInfo?)](./xctsourcecodeframe/init%28address,symbolinfo%29.md)
  Initializes an instance with a frame address and symbol information.
- [convenience init(address: UInt64)](./xctsourcecodeframe/init%28address%29.md)
  Initializes an instance with a frame address.
### Frame Information
- [var address: UInt64](./xctsourcecodeframe/address.md)
  An address that represents a specific frame in a call stack.
- [var symbolInfo: XCTSourceCodeSymbolInfo?](./xctsourcecodeframe/symbolinfo.md)
  Symbolication information for the referenced frame.
- [var symbolicationError: (any Error)?](./xctsourcecodeframe/symbolicationerror.md)
  An optional error that describes a failed symbolication attempt.
- [func symbolInfo() throws -> XCTSourceCodeSymbolInfo](./xctsourcecodeframe/symbolinfo%28%29.md)
  Attempts to get symbol information for the address.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Test Failures
- [struct XCTIssue](./xctissue-swift.struct.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTIssueReference](./xctissuereference.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTMutableIssue](./xctmutableissue.md)
  A mutable object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTSourceCodeContext](./xctsourcecodecontext.md)
  An object that contains call stack and source code location details to provide context for a point of execution in a test.
- [class XCTSourceCodeLocation](./xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](./xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodeframe)*