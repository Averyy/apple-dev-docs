# testSuite(_:didRecord:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Notifies the observer when a test suite reports an issue.

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```swift
optional func testSuite(_ testSuite: XCTestSuite, didRecord issue: XCTIssue)
```

*macOS*

```swift
optional func testSuite(_ testSuite: XCTestSuite, didRecord issue: XCTIssueReference)
```

```objc
- (void) testSuite:(XCTestSuite *) testSuite didRecordIssue:(XCTIssue *) issue;
```

## Parameters

- `testSuite`: The test suite with the issue.
- `issue`: The issue to record.

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
- [func testCase(XCTestCase, didFailWithDescription: String, inFile: String?, atLine: Int)](./testcase%28_,didfailwithdescription,infile,atline%29.md)
  Notifies the observer when a test case reports a failure.
- [func testCaseDidFinish(XCTestCase)](./testcasedidfinish%28_%29.md)
  Notifies the observer immediately after a test case finishes executing.
- [func testSuite(XCTestSuite, didRecord: XCTExpectedFailure)](./testsuite%28_,didrecord%29-1xjkv.md)
  Notifies the observer when a test suite records an expected failure.
- [func testSuite(XCTestSuite, didFailWithDescription: String, inFile: String?, atLine: Int)](./testsuite%28_,didfailwithdescription,infile,atline%29.md)
  Notifies the observer when a test suite reports a failure.
- [func testSuiteDidFinish(XCTestSuite)](./testsuitedidfinish%28_%29.md)
  Notifies the observer immediately after a test suite finishes executing.
- [func testBundleDidFinish(Bundle)](./testbundledidfinish%28_%29.md)
  Notifies the observer immediately after all tests in a test bundle finish executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobservation/testsuite(_:didrecord:)-3rk9k)*