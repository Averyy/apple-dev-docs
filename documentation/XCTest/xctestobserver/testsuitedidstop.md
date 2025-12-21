# testSuiteDidStop(_:)

**Framework**: XCTest  
**Kind**: method

Notifies the observer when a test suite stops.

## Declaration

```swift
func testSuiteDidStop(_ testRun: XCTestRun!)
```

## Parameters

- `testRun`: The test run object calling this method.

## See Also

- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](xctestobserver/testcasedidfail(_:withdescription:infile:atline:).md)
  Notifies the observer when a test case fails.
- [func testCaseDidStart(XCTestRun!)](xctestobserver/testcasedidstart(_:).md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](xctestobserver/testcasedidstop(_:).md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](xctestobserver/testsuitedidstart(_:).md)
  Notifies the observer when a test suite starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testsuitedidstop(_:))*