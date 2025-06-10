# XCTestObservation

**Framework**: XCTest  
**Kind**: protocol

A protocol that defines methods the test runner calls in response to significant events during test runs.

## Declaration

```swift
protocol XCTestObservation : NSObjectProtocol
```

#### Overview

The system calls the notification methods for [`XCTestObservation`](xctestobservation.md) in the following sequence for a test bundle:

1. [`testBundleWillStart(_:)`](xctestobservation/testbundlewillstart(_:).md) — exactly once per test bundle
2. [`testSuiteWillStart(_:)`](xctestobservation/testsuitewillstart(_:).md) — exactly once per test suite
3. [`testCaseWillStart(_:)`](xctestobservation/testcasewillstart(_:).md) — exactly once per test case
4. [`testCase(_:didRecord:)`](xctestobservation/testcase(_:didrecord:)-4cou6.md)  — for each test failure, zero or more times per test case at any point between test case start and finish
5. [`testCase(_:didRecord:)`](xctestobservation/testcase(_:didrecord:)-8k955.md)  — for each expected test failure, zero or more times per test case at any point between test case start and finish
6. [`testCaseDidFinish(_:)`](xctestobservation/testcasedidfinish(_:).md) — exactly once per test case
7. [`testSuite(_:didRecord:)`](xctestobservation/testsuite(_:didrecord:)-3rk9k.md) — for each test failure, zero or more times per test suite at any point between test suite start and finish
8. [`testSuite(_:didRecord:)`](xctestobservation/testsuite(_:didrecord:)-1xjkv.md) — for each expected test failure, zero or more times per test suite at any point between test suite start and finish
9. [`testSuiteDidFinish(_:)`](xctestobservation/testsuitedidfinish(_:).md) — exactly once per test suite
10. [`testBundleDidFinish(_:)`](xctestobservation/testbundledidfinish(_:).md) — exactly once per test bundle

See [`XCTestObservationCenter`](xctestobservationcenter.md) for details about registering and removing test observers.

## Topics

### Observation Methods
- [func testBundleWillStart(Bundle)](xctestobservation/testbundlewillstart(_:).md)
  Notifies the observer immediately before any tests in a test bundle begin.
- [func testSuiteWillStart(XCTestSuite)](xctestobservation/testsuitewillstart(_:).md)
  Notifies the observer immediately before a test suite begins executing.
- [func testCaseWillStart(XCTestCase)](xctestobservation/testcasewillstart(_:).md)
  Notifies the observer immediately before a test case begins executing.
- [func testCase(XCTestCase, didRecord: XCTIssue)](xctestobservation/testcase(_:didrecord:)-4cou6.md)
  Notifies the observer when a test case reports an issue.
- [func testCase(XCTestCase, didRecord: XCTExpectedFailure)](xctestobservation/testcase(_:didrecord:)-8k955.md)
  Notifies the observer when a test case records an expected failure.
- [func testCase(XCTestCase, didFailWithDescription: String, inFile: String?, atLine: Int)](xctestobservation/testcase(_:didfailwithdescription:infile:atline:).md)
  Notifies the observer when a test case reports a failure.
- [func testCaseDidFinish(XCTestCase)](xctestobservation/testcasedidfinish(_:).md)
  Notifies the observer immediately after a test case finishes executing.
- [func testSuite(XCTestSuite, didRecord: XCTIssue)](xctestobservation/testsuite(_:didrecord:)-3rk9k.md)
  Notifies the observer when a test suite reports an issue.
- [func testSuite(XCTestSuite, didRecord: XCTExpectedFailure)](xctestobservation/testsuite(_:didrecord:)-1xjkv.md)
  Notifies the observer when a test suite records an expected failure.
- [func testSuite(XCTestSuite, didFailWithDescription: String, inFile: String?, atLine: Int)](xctestobservation/testsuite(_:didfailwithdescription:infile:atline:).md)
  Notifies the observer when a test suite reports a failure.
- [func testSuiteDidFinish(XCTestSuite)](xctestobservation/testsuitedidfinish(_:).md)
  Notifies the observer immediately after a test suite finishes executing.
- [func testBundleDidFinish(Bundle)](xctestobservation/testbundledidfinish(_:).md)
  Notifies the observer immediately after all tests in a test bundle finish executing.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XCTestObservationCenter](xctestobservationcenter.md)
  Provides information about the progress of test runs to registered observers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation)*