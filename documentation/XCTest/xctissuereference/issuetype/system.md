# XCTIssueReference.IssueType.system

**Framework**: XCTest  
**Kind**: case  
**Role**: Case

A test failure due to an internal failure in the testing framework.

## Declaration

```swift
case system
```

```c
XCTIssueTypeSystem
```

#### Discussion

This type of failure could happen if `XCUIApplication` was unable to launch or terminate an app, or if `XCUIElementQuery` was unable to complete a query.

## See Also

### Issue Types
- [XCTIssueReference.IssueType.assertionFailure](./assertionfailure.md)
  A test failure due to a failed test assertion or related API.
- [XCTIssueReference.IssueType.performanceRegression](./performanceregression.md)
  A test failure due to a performance regression.
- [XCTIssueReference.IssueType.thrownError](./thrownerror.md)
  A test failure when the test throws an error in Swift.
- [XCTIssueReference.IssueType.uncaughtException](./uncaughtexception.md)
  A test failure when code throws an exception and doesn’t catch it.
- [XCTIssueReference.IssueType.unmatchedExpectedFailure](./unmatchedexpectedfailure.md)
  A test failure due to an expected test failure that doesn’t occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/issuetype/system)*