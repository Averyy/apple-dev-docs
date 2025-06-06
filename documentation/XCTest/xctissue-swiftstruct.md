# XCTIssue

**Framework**: Xctest  
**Kind**: struct

An object that represents a test failure, and includes source code call stacks for test reporting and investigation.

## Declaration

```swift
struct XCTIssue
```

## Topics

### Initializers
- [init(type: XCTIssue.IssueType, compactDescription: String, detailedDescription: String?, sourceCodeContext: XCTSourceCodeContext, associatedError: (any Error)?, attachments: [XCTAttachment])](xctissue-swift.struct/init(type:compactdescription:detaileddescription:sourcecodecontext:associatederror:attachments:).md)
  Creates an issue for a test failure, with descriptions, source code location, error, and attachments.
### Issue Types
- [typealias IssueType](xctissue-swift.struct/issuetype.md)
  Constants that indicate types of test failures, such as assertion failures, performance regressions, or thrown errors.
### Issue Details
- [var type: XCTIssue.IssueType](xctissue-swift.struct/type.md)
  A value for classifying an issue that occurs during testing.
- [var compactDescription: String](xctissue-swift.struct/compactdescription.md)
  A concise description of the issue with no transient data, suitable for use in test run summaries and results aggregation across multiple test runs.
- [var detailedDescription: String?](xctissue-swift.struct/detaileddescription.md)
  A detailed description of the issue that may include transient data, such as numbers, object identifiers, and timestamps, to help diagnose the issue.
- [var sourceCodeContext: XCTSourceCodeContext](xctissue-swift.struct/sourcecodecontext.md)
  The source code location for the issue, including the filename, line number, and call stack.
- [var associatedError: (any Error)?](xctissue-swift.struct/associatederror.md)
  An optional error to associate with a test issue.
- [var attachments: [XCTAttachment]](xctissue-swift.struct/attachments.md)
  An array of data that augments an issue, such as files, images, screenshots, data blobs, or ZIP files.
- [func add(XCTAttachment)](xctissue-swift.struct/add(_:).md)
  Adds supporting data to an issue.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [class XCTIssueReference](xctissuereference.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTMutableIssue](xctmutableissue.md)
  A mutable object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTSourceCodeContext](xctsourcecodecontext.md)
  An object that contains call stack and source code location details to provide context for a point of execution in a test.
- [class XCTSourceCodeFrame](xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeLocation](xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissue-swift.struct)*