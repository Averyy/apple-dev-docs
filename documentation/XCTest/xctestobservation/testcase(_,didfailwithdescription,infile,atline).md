# testCase(_:didFailWithDescription:inFile:atLine:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Notifies the observer when a test case reports a failure.

> **Deprecated**: Use [`testCase(_:didRecord:)`](./testcase%28_,didrecord%29-4cou6.md) instead. If you implement both this method and [`testCase(_:didRecord:)`](./testcase%28_,didrecord%29-4cou6.md), the test will not call this method.

## Declaration

```swift
optional func testCase(_ testCase: XCTestCase, didFailWithDescription description: String, inFile filePath: String?, atLine lineNumber: Int)
```

```objc
- (void) testCase:(XCTestCase *) testCase didFailWithDescription:(NSString *) description inFile:(NSString *) filePath atLine:(NSUInteger) lineNumber;
```

## Parameters

- `testCase`: The test case that reported a failure. Additional information about the test case can be retrieved from the test case’s associated [`XCTestRun`](../xctestrun.md).
- `description`: A textual description of the failure.
- `filePath`: The path to the file in the failure occurred, or `nil` if the file path is unknown.
- `lineNumber`: The line number on which the failure was reported.

## See Also

### Observation Methods
- [func testBundleWillStart(Bundle)](./testbundlewillstart%28_%29.md)
  Notifies the observer immediately before any tests in a test bundle begin.
- [func testSuiteWillStart(XCTestSuite)](./testsuitewillstart%28_%29.md)
  Notifies the observer immediately before a test suite begins executing.
- [func testCaseWillStart(XCTestCase)](./testcasewillstart%28_%29.md)
  Notifies the observer immediately before a test case begins executing.
- [func testCase(XCTestCase, didRecord: XCTIssue)](./testcase%28_,didrecord%29-4cou6.md)
  Notifies the observer when a test case reports an issue.
- [func testCase(XCTestCase, didRecord: XCTExpectedFailure)](./testcase%28_,didrecord%29-8k955.md)
  Notifies the observer when a test case records an expected failure.
- [func testCaseDidFinish(XCTestCase)](./testcasedidfinish%28_%29.md)
  Notifies the observer immediately after a test case finishes executing.
- [func testSuite(XCTestSuite, didRecord: XCTIssue)](./testsuite%28_,didrecord%29-3rk9k.md)
  Notifies the observer when a test suite reports an issue.
- [func testSuite(XCTestSuite, didRecord: XCTExpectedFailure)](./testsuite%28_,didrecord%29-1xjkv.md)
  Notifies the observer when a test suite records an expected failure.
- [func testSuite(XCTestSuite, didFailWithDescription: String, inFile: String?, atLine: Int)](./testsuite%28_,didfailwithdescription,infile,atline%29.md)
  Notifies the observer when a test suite reports a failure.
- [func testSuiteDidFinish(XCTestSuite)](./testsuitedidfinish%28_%29.md)
  Notifies the observer immediately after a test suite finishes executing.
- [func testBundleDidFinish(Bundle)](./testbundledidfinish%28_%29.md)
  Notifies the observer immediately after all tests in a test bundle finish executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation/testcase(_:didfailwithdescription:infile:atline:))*