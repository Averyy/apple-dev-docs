# continueAfterFailure

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a test method should continue running after a failure occurs.

## Declaration

```swift
var continueAfterFailure: Bool { get set }
```

```objc
@property BOOL continueAfterFailure;
```

#### Discussion

The default is [`true`](../../Swift/true.md). Set this property to [`false`](../../Swift/false.md) within a test method to end execution of that method as soon as a failure occurs. Other test methods in the suite may still execute after a test fails.

## See Also

### Managing Test Case Execution
- [class var runsForEachTargetApplicationUIConfiguration: Bool](./runsforeachtargetapplicationuiconfiguration.md)
  A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.
- [var executionTimeAllowance: TimeInterval](./executiontimeallowance.md)
  The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/continueafterfailure)*