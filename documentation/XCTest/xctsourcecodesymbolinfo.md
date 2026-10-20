# XCTSourceCodeSymbolInfo

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that contains symbolication information for a specified frame in a call stack.

## Declaration

```swift
class XCTSourceCodeSymbolInfo
```

```objc
@interface XCTSourceCodeSymbolInfo : NSObject
```

## Topics

### Initializers
- [init(imageName: String, symbolName: String, location: XCTSourceCodeLocation?)](./xctsourcecodesymbolinfo/init%28imagename,symbolname,location%29.md)
  Initializes an instance with a binary image name, source code location, and symbol name.
### Symbol Information
- [var imageName: String](./xctsourcecodesymbolinfo/imagename.md)
  The name of the binary image that contains the symbolicated code.
- [var location: XCTSourceCodeLocation?](./xctsourcecodesymbolinfo/location.md)
  A representation of a location in source code where a test issue occurred.
- [var symbolName: String](./xctsourcecodesymbolinfo/symbolname.md)
  A string that represents a human-readable symbol in source code.

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
- [class XCTSourceCodeFrame](./xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeLocation](./xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodesymbolinfo)*