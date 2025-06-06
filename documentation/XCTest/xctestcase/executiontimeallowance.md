# executionTimeAllowance

**Framework**: Xctest  
**Kind**: property

The number of seconds, rounded up to the nearest minute, for a test to run before it fails with a timeout error.

## Declaration

```swift
var executionTimeAllowance: TimeInterval { get set }
```

#### Discussion

If the duration of a test exceeds this value, it’s marked as a failure and the next test runs. The default value is 600 seconds, or 10 minutes. The test rounds up the value you supply to the nearest minute.

Use this property to guard against long-running or hanging tests; use performance tests to precisely measure execution time and guard against regressions.

To use this setting, enable timeouts in your test plan or set the `-test-timeouts-enabled` option to `YES` when using `xcodebuild`.

> **Note**:  The test may run for less time than you specify if you customize the Maximum Test Execution Time Allowance setting in the test plan, or if you pass the `-maximum-test-execution-time-allowance` option to `xcodebuild`.

## See Also

- [class var runsForEachTargetApplicationUIConfiguration: Bool](xctestcase/runsforeachtargetapplicationuiconfiguration.md)
  A Boolean value that indicates whether your UI tests run once for each possible combination of orientation, localization, and other appearance settings your app supports.
- [var continueAfterFailure: Bool](xctestcase/continueafterfailure.md)
  A Boolean value that indicates whether a test method should continue running after a failure occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcase/executiontimeallowance)*