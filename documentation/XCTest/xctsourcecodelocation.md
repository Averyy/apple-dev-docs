# XCTSourceCodeLocation

**Framework**: Xctest  
**Kind**: class

An object that contains a file URL and line number that represents a distinct location in source code.

## Declaration

```swift
class XCTSourceCodeLocation
```

## Topics

### Initializers
- [init(fileURL: URL, lineNumber: Int)](xctsourcecodelocation/init(fileurl:linenumber:).md)
  Initializes a new instance with a file URL and a line number.
- [convenience init(filePath: String, lineNumber: Int)](xctsourcecodelocation/init(filepath:linenumber:)-3hzmr.md)
  Initializes a new instance with a file path and a line number.
- [convenience init(filePath: StaticString, lineNumber: UInt)](xctsourcecodelocation/init(filepath:linenumber:)-8qw52.md)
  Initializes a new instance with a file path and a line number.
### Source Location Information
- [var fileURL: URL](xctsourcecodelocation/fileurl.md)
  A file URL that represents the file-system location of the source code file.
- [var lineNumber: Int](xctsourcecodelocation/linenumber.md)
  An integer that represents a line of code in a source code file.

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
- [class XCTSourceCodeFrame](xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctsourcecodelocation)*