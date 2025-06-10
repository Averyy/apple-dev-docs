# testCase(_:didRecord:)

**Framework**: XCTest  
**Kind**: method

Notifies the observer when a test case reports an issue.

## Declaration

```swift
optional func testCase(_ testCase: XCTestCase, didRecord issue: XCTIssue)
```

## Parameters

- `testCase`: The test case with the issue.
- `issue`: The issue to record.

## See Also

- [func testBundleWillStart(Bundle)](xctestobservation/testbundlewillstart(_:).md)
  Notifies the observer immediately before any tests in a test bundle begin.
- [func testSuiteWillStart(XCTestSuite)](xctestobservation/testsuitewillstart(_:).md)
  Notifies the observer immediately before a test suite begins executing.
- [func testCaseWillStart(XCTestCase)](xctestobservation/testcasewillstart(_:).md)
  Notifies the observer immediately before a test case begins executing.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation/testcase(_:didrecord:)-4cou6)*