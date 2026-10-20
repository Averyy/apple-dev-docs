# unexpectedExceptionCount

**Framework**: XCTest  
**Kind**: property  
**Role**: Instance Property

The number of uncaught exceptions during the run.

## Declaration

```swift
var unexpectedExceptionCount: Int { get }
```

```objc
@property (readonly) NSUInteger unexpectedExceptionCount;
```

## See Also

### Gathering Test Outcomes
- [var hasSucceeded: Bool](./hassucceeded.md)
  A Boolean value that returns true if all tests in the run completed without recording any failures; otherwise, false.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun/unexpectedexceptioncount)*