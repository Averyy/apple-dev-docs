# stop()

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Stops a test run.

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

#### Discussion

This method must not be called unless the run has been started, and must not be called more than once.

## See Also

### Performing Test Runs
- [func start()](./start%28%29.md)
  Starts a test run.
- [func record(XCTIssue)](./record%28_%29.md)
  Records an issue during test execution for the test run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/stop())*