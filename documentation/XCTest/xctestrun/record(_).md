# record(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Records an issue during test execution for the test run.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
func record(_ issue: XCTIssue)
```

*macOS*

```swift
func record(_ issue: XCTIssueReference)
```

```objc
- (void) recordIssue:(XCTIssue *) issue;
```

#### Discussion

The test run records a failure or other issue during test execution with this method. Override to customize the issue, and call `super` unless you want to suppress the issue.

## Parameters

- `issue`: The test issue to record.

## See Also

### Performing Test Runs
- [func start()](./start%28%29.md)
  Starts a test run.
- [func stop()](./stop%28%29.md)
  Stops a test run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/record(_:))*