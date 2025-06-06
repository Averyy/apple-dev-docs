# XCTIssueReference

**Framework**: Xctest  
**Kind**: class

An object that represents a test failure, and includes source code call stacks for test reporting and investigation.

## Declaration

```swift
class XCTIssueReference
```

#### Overview

In Swift, `XCTIssueReference` bridges to the Objective-C class `XCTIssue`. When you need reference semantics in your Swift test handling, use `XCTIssueReference`; otherwise, use the Swift value semantic [`XCTIssue`](xctissue-swift.struct.md). In Objective-C, `XCTIssue` supports bridging to Swift with `XCTIssueReference`.

## Topics

### Initializers
- [convenience init(type: XCTIssueReference.IssueType, compactDescription: String)](xctissuereference/init(type:compactdescription:).md)
  Creates an issue with a compact description for a test failure.
- [init(type: XCTIssueReference.IssueType, compactDescription: String, detailedDescription: String?, sourceCodeContext: XCTSourceCodeContext, associatedError: (any Error)?, attachments: [XCTAttachment])](xctissuereference/init(type:compactdescription:detaileddescription:sourcecodecontext:associatederror:attachments:).md)
  Creates an issue for a test failure, with descriptions, source code location, error, and attachments.
### Issue Types
- [XCTIssueReference.IssueType](xctissuereference/issuetype.md)
  Constants that indicate types of test failures, such as assertion failures, performance regressions, or thrown errors.
### Issue Details
- [var type: XCTIssueReference.IssueType](xctissuereference/type.md)
  A value for classifying an issue that occurs during testing.
- [var compactDescription: String](xctissuereference/compactdescription.md)
  A concise description of the issue with no transient data, suitable for use in test run summaries and results aggregation across multiple test runs.
- [var detailedDescription: String?](xctissuereference/detaileddescription.md)
  A detailed description of the issue that may include transient data, such as numbers, object identifiers, and timestamps, to help diagnose the issue.
- [var sourceCodeContext: XCTSourceCodeContext](xctissuereference/sourcecodecontext.md)
  The source code location for the issue, including the filename, line number, and call stack.
- [var associatedError: (any Error)?](xctissuereference/associatederror.md)
  An optional error to associate with a test issue.
- [var attachments: [XCTAttachment]](xctissuereference/attachments.md)
  An array of data that augments a test issue, such as files, images, screenshots, data blobs, or ZIP files.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [XCTMutableIssue](xctmutableissue.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference)*