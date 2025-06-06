# XCTestRun

**Framework**: Xctest  
**Kind**: class

A base class for collecting information about a specific execution of a test.

## Declaration

```swift
class XCTestRun
```

#### Overview

`XCTestRun` classifies failures in explicit test assertions as , and failures from unrelated or uncaught exceptions as .

## Topics

### Creating Test Runs
- [init(test: XCTest)](xctestrun/init(test:).md)
  Creates a new test run for the provided test.
### Performing Test Runs
- [func start()](xctestrun/start.md)
  Starts a test run.
- [func stop()](xctestrun/stop.md)
  Stops a test run.
- [func record(XCTIssue)](xctestrun/record(_:).md)
  Records an issue during test execution for the test run.
### Tracking Test Durations
- [var startDate: Date?](xctestrun/startdate.md)
  The date and time when the test run started, or no value if the test hasn’t run.
- [var stopDate: Date?](xctestrun/stopdate.md)
  The date and time when the test run stopped, or no value if the test hasn’t run.
- [var testDuration: TimeInterval](xctestrun/testduration.md)
  The number of seconds that elapse between when the run starts and when it stops.
- [var totalDuration: TimeInterval](xctestrun/totalduration.md)
  The number of seconds that elapse between when the run starts and when it stops.
### Gathering Test Outcomes
- [var hasSucceeded: Bool](xctestrun/hassucceeded.md)
  A Boolean value that returns true if all tests in the run completed without recording any failures; otherwise, false.
- [var hasBeenSkipped: Bool](xctestrun/hasbeenskipped.md)
  A Boolean value that indicates a skipped test.
- [var executionCount: Int](xctestrun/executioncount.md)
  The number of test executions during the run.
- [var failureCount: Int](xctestrun/failurecount.md)
  The number of test failures during the run.
- [var skipCount: Int](xctestrun/skipcount.md)
  The number of skipped tests during the run.
- [var test: XCTest](xctestrun/test.md)
  The test instance for the test run.
- [var testCaseCount: Int](xctestrun/testcasecount.md)
  The number of tests in the run.
- [var totalFailureCount: Int](xctestrun/totalfailurecount.md)
  The number of test failures and uncaught exceptions during the run.
- [var unexpectedExceptionCount: Int](xctestrun/unexpectedexceptioncount.md)
  The number of uncaught exceptions during the run.
### Deprecated
- [func recordFailure(withDescription: String, inFile: String?, atLine: Int, expected: Bool)](xctestrun/recordfailure(withdescription:infile:atline:expected:).md)
  Records a failure during test execution for the test run.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [XCTestCaseRun](xctestcaserun.md)
- [XCTestSuiteRun](xctestsuiterun.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XCTestCaseRun](xctestcaserun.md)
  An object that collects information about a specific execution of a test case.
- [class XCTestSuiteRun](xctestsuiterun.md)
  An object that collects information about a specific execution of a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestrun)*