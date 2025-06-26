# record(_:)

**Framework**: XCTest  
**Kind**: method

Records an issue during test execution for the test run.

## Declaration

```swift
func record(_ issue: XCTIssue)
```

#### Discussion

The test run records a failure or other issue during test execution with this method. Override to customize the issue, and call `super` unless you want to suppress the issue.

## Parameters

- `issue`: The test issue to record.

## See Also

- [func start()](xctestrun/start.md)
  Starts a test run.
- [func stop()](xctestrun/stop.md)
  Stops a test run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/record(_:))*