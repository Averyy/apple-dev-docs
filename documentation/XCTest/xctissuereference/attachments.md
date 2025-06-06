# attachments

**Framework**: Xctest  
**Kind**: property

An array of data that augments a test issue, such as files, images, screenshots, data blobs, or ZIP files.

## Declaration

```swift
var attachments: [XCTAttachment] { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/attachments)*