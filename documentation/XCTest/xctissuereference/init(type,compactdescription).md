# init(type:compactDescription:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

Creates an issue with a compact description for a test failure.

## Declaration

```swift
convenience init(type: XCTIssueReference.IssueType, compactDescription: String)
```

```objc
- (instancetype) initWithType:(XCTIssueType) type compactDescription:(NSString *) compactDescription;
```

## Parameters

- `type`: A value for classifying an issue that occurs during testing.
- `compactDescription`: A concise description of the issue that doesn’t include transient data and is suitable for use in test run summaries and for aggregation of results across multiple test runs.

## See Also

### Initializers
- [init(type: XCTIssueReference.IssueType, compactDescription: String, detailedDescription: String?, sourceCodeContext: XCTSourceCodeContext, associatedError: (any Error)?, attachments: [XCTAttachment])](./init%28type,compactdescription,detaileddescription,sourcecodecontext,associatederror,attachments%29.md)
  Creates an issue for a test failure, with descriptions, source code location, error, and attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/init(type:compactdescription:))*