# testCaseDidFail(_:withDescription:inFile:atLine:)

**Framework**: XCTest  
**Kind**: method

Notifies the observer when a test case fails.

**Availability**:
- Unknown ?+ - Deprecated

## Declaration

```swift
func testCaseDidFail(_ testRun: XCTestRun!, withDescription description: String!, inFile filePath: String!, atLine lineNumber: Int)
```

## Parameters

- `testRun`: The test run object that calls this method.
- `description`: A string description of the failed test.
- `filePath`: A string that represents a file path to a source code file when the test encounters a failure.
- `lineNumber`: An integer value that represents the line number in the source code file when the test encounters a failure.

## See Also

- [func testCaseDidStart(XCTestRun!)](xctestobserver/testcasedidstart(_:).md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](xctestobserver/testcasedidstop(_:).md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](xctestobserver/testsuitedidstart(_:).md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](xctestobserver/testsuitedidstop(_:).md)
  Notifies the observer when a test suite stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testcasedidfail(_:withdescription:infile:atline:))*