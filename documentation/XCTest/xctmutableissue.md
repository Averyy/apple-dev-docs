# XCTMutableIssue

**Framework**: XCTest  
**Kind**: class

A mutable object that represents a test failure, and includes source code call stacks for test reporting and investigation.

## Declaration

```swift
class XCTMutableIssue
```

## Topics

### Issue Details
- [var type: XCTIssueReference.IssueType](xctmutableissue/type.md)
  A value for classifying an issue that occurs during testing.
- [var compactDescription: String](xctmutableissue/compactdescription.md)
  A concise description of the issue with no transient data, suitable for use in test run summaries and results aggregation across multiple test runs.
- [var detailedDescription: String?](xctmutableissue/detaileddescription.md)
  A detailed description of the issue that may include transient data, such as numbers, object identifiers, and timestamps, to help diagnose the issue.
- [var sourceCodeContext: XCTSourceCodeContext](xctmutableissue/sourcecodecontext.md)
  The source code location for the issue, including the filename, line number, and call stack.
- [var associatedError: (any Error)?](xctmutableissue/associatederror.md)
  An optional error to associate with a test issue.
- [var attachments: [XCTAttachment]](xctmutableissue/attachments.md)
  An array of data that augments an issue, such as files, images, screenshots, data blobs, or ZIP files.
- [func add(XCTAttachment)](xctmutableissue/add(_:).md)
  Adds supporting data to an issue.
### Instance Properties
- [var severity: XCTIssueReference.Severity](xctmutableissue/severity.md)

## Relationships

### Inherits From
- [XCTIssueReference](xctissuereference.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [struct XCTIssue](xctissue-swift.struct.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTIssueReference](xctissuereference.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTSourceCodeContext](xctsourcecodecontext.md)
  An object that contains call stack and source code location details to provide context for a point of execution in a test.
- [class XCTSourceCodeFrame](xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeLocation](xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmutableissue)*