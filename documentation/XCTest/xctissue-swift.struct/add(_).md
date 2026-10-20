# add(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Adds supporting data to an issue.

## Declaration

```swift
mutating func add(_ attachment: XCTAttachment)
```

## Parameters

- `attachment`: A data item that augments an issue, such as a file, image, screenshot, data blob, or ZIP file.

## See Also

### Issue Details
- [var type: XCTIssue.IssueType](./type.md)
  A value for classifying an issue that occurs during testing.
- [var compactDescription: String](./compactdescription.md)
  A concise description of the issue with no transient data, suitable for use in test run summaries and results aggregation across multiple test runs.
- [var detailedDescription: String?](./detaileddescription.md)
  A detailed description of the issue that may include transient data, such as numbers, object identifiers, and timestamps, to help diagnose the issue.
- [var sourceCodeContext: XCTSourceCodeContext](./sourcecodecontext.md)
  The source code location for the issue, including the filename, line number, and call stack.
- [var associatedError: (any Error)?](./associatederror.md)
  An optional error to associate with a test issue.
- [var attachments: [XCTAttachment]](./attachments.md)
  An array of data that augments an issue, such as files, images, screenshots, data blobs, or ZIP files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissue-swift.struct/add(_:))*