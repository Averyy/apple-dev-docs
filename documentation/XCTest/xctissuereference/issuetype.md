# XCTIssueReference.IssueType

**Framework**: XCTest  
**Kind**: enum

Constants that indicate types of test failures, such as assertion failures, performance regressions, or thrown errors.

## Declaration

```swift
enum IssueType
```

## Topics

### Issue Types
- [XCTIssueReference.IssueType.assertionFailure](xctissuereference/issuetype/assertionfailure.md)
  A test failure due to a failed test assertion or related API.
- [XCTIssueReference.IssueType.performanceRegression](xctissuereference/issuetype/performanceregression.md)
  A test failure due to a performance regression.
- [XCTIssueReference.IssueType.system](xctissuereference/issuetype/system.md)
  A test failure due to an internal failure in the testing framework.
- [XCTIssueReference.IssueType.thrownError](xctissuereference/issuetype/thrownerror.md)
  A test failure when the test throws an error in Swift.
- [XCTIssueReference.IssueType.uncaughtException](xctissuereference/issuetype/uncaughtexception.md)
  A test failure when code throws an exception and doesn’t catch it.
- [XCTIssueReference.IssueType.unmatchedExpectedFailure](xctissuereference/issuetype/unmatchedexpectedfailure.md)
  A test failure due to an expected test failure that doesn’t occur.
### Initializers
- [init?(rawValue: Int)](xctissuereference/issuetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/issuetype)*