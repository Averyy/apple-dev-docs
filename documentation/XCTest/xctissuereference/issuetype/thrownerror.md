# XCTIssueReference.IssueType.thrownError

**Framework**: XCTest  
**Kind**: case  
**Role**: Case

A test failure when the test throws an error in Swift.

## Declaration

```swift
case thrownError
```

```c
XCTIssueTypeThrownError
```

## Discussion

This could also occur if an Objective-C test uses the form `-(BOOL)testExample:(NSError **)outError` and returns `NO` with a non-`nil` out error.

## See Also

### Issue Types
- [XCTIssueReference.IssueType.assertionFailure](./assertionfailure.md)
  A test failure due to a failed test assertion or related API.
- [XCTIssueReference.IssueType.performanceRegression](./performanceregression.md)
  A test failure due to a performance regression.
- [XCTIssueReference.IssueType.system](./system.md)
  A test failure due to an internal failure in the testing framework.
- [XCTIssueReference.IssueType.uncaughtException](./uncaughtexception.md)
  A test failure when code throws an exception and doesn’t catch it.
- [XCTIssueReference.IssueType.unmatchedExpectedFailure](./unmatchedexpectedfailure.md)
  A test failure due to an expected test failure that doesn’t occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctissuereference/issuetype/thrownerror)*