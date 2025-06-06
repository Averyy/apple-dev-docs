# type

**Framework**: Xctest  
**Kind**: property

A value for classifying an issue that occurs during testing.

## Declaration

```swift
var type: XCTIssueReference.IssueType { get set }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctmutableissue/type)*