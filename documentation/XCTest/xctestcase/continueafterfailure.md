# continueAfterFailure

**Framework**: XCTest  
**Kind**: property

A Boolean value that indicates whether a test method should continue running after a failure occurs.

## Declaration

```swift
var continueAfterFailure: Bool { get set }
```

#### Discussion

The default is [`true`](https://developer.apple.com/documentation/Swift/true). Set this property to [`false`](https://developer.apple.com/documentation/Swift/false) within a test method to end execution of that method as soon as a failure occurs. Other test methods in the suite may still execute after a test fails.

## See Also

- [class var runsForEachTargetApplicationUIConfiguration: Bool](xctestcase/runsforeachtargetapplicationuiconfiguration.md)
  A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.
- [var executionTimeAllowance: TimeInterval](xctestcase/executiontimeallowance.md)
  The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/continueafterfailure)*