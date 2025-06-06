# testCaseDidStart(_:)

**Framework**: Xctest  
**Kind**: method

Notifies the observer when a test case starts.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
func testCaseDidStart(_ testRun: XCTestRun!)
```

## Parameters

- `testRun`: The test run object that calls this method.

## See Also

- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](xctestobserver/testcasedidfail(_:withdescription:infile:atline:).md)
  Notifies the observer when a test case fails.
- [func testCaseDidStop(XCTestRun!)](xctestobserver/testcasedidstop(_:).md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](xctestobserver/testsuitedidstart(_:).md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](xctestobserver/testsuitedidstop(_:).md)
  Notifies the observer when a test suite stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testcasedidstart(_:))*