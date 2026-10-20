# hasSucceeded

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

A Boolean value that returns true if all tests in the run completed without recording any failures; otherwise, false.

## Declaration

```swift
var hasSucceeded: Bool { get }
```

```objc
@property (readonly) BOOL hasSucceeded;
```

## See Also

### Gathering Test Outcomes
- [var hasBeenSkipped: Bool](./hasbeenskipped.md)
  A Boolean value that indicates a skipped test.
- [var executionCount: Int](./executioncount.md)
  The number of test executions during the run.
- [var failureCount: Int](./failurecount.md)
  The number of test failures during the run.
- [var skipCount: Int](./skipcount.md)
  The number of skipped tests during the run.
- [var test: XCTest](./test.md)
  The test instance for the test run.
- [var testCaseCount: Int](./testcasecount.md)
  The number of tests in the run.
- [var totalFailureCount: Int](./totalfailurecount.md)
  The number of test failures and uncaught exceptions during the run.
- [var unexpectedExceptionCount: Int](./unexpectedexceptioncount.md)
  The number of uncaught exceptions during the run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/hassucceeded)*