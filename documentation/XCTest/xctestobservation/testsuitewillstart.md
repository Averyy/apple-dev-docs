# testSuiteWillStart(_:)

**Framework**: Xctest  
**Kind**: method

Notifies the observer immediately before a test suite begins executing.

## Declaration

```swift
optional func testSuiteWillStart(_ testSuite: XCTestSuite)
```

## Parameters

- `testSuite`: The test suite that is about to start. Additional information about the suite can be retrieved from the test suite’s associated  .

## See Also

- [func testBundleWillStart(Bundle)](xctestobservation/testbundlewillstart(_:).md)
  Notifies the observer immediately before any tests in a test bundle begin.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation/testsuitewillstart(_:))*