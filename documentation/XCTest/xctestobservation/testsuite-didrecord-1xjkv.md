# testSuite(_:didRecord:)

**Framework**: Xctest  
**Kind**: method

Notifies the observer when a test suite records an expected failure.

## Declaration

```swift
optional func testSuite(_ testSuite: XCTestSuite, didRecord expectedFailure: XCTExpectedFailure)
```

## Parameters

- `testSuite`: The test suite with the expected failure.
- `expectedFailure`: The expected failure to record.

## See Also

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
- [func testSuite(XCTestSuite, didFailWithDescription: String, inFile: String?, atLine: Int)](xctestobservation/testsuite(_:didfailwithdescription:infile:atline:).md)
  Notifies the observer when a test suite reports a failure.
- [func testSuiteDidFinish(XCTestSuite)](xctestobservation/testsuitedidfinish(_:).md)
  Notifies the observer immediately after a test suite finishes executing.
- [func testBundleDidFinish(Bundle)](xctestobservation/testbundledidfinish(_:).md)
  Notifies the observer immediately after all tests in a test bundle finish executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation/testsuite(_:didrecord:)-1xjkv)*