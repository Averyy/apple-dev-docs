# init(type:compactDescription:detailedDescription:sourceCodeContext:associatedError:attachments:severity:)

**Framework**: XCTest  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(type: XCTIssueReference.IssueType, compactDescription: String, detailedDescription: String?, sourceCodeContext: XCTSourceCodeContext, associatedError: (any Error)?, attachments: [XCTAttachment], severity: XCTIssueReference.Severity)
```

```objc
- (instancetype) initWithType:(XCTIssueType) type compactDescription:(NSString *) compactDescription detailedDescription:(NSString *) detailedDescription sourceCodeContext:(XCTSourceCodeContext *) sourceCodeContext associatedError:(NSError *) associatedError attachments:(NSArray<XCTAttachment *> *) attachments severity:(XCTIssueSeverity) severity;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/init(type:compactdescription:detaileddescription:sourcecodecontext:associatederror:attachments:severity:))*