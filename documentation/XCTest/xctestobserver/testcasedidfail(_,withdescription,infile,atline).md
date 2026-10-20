# testCaseDidFail(_:withDescription:inFile:atLine:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Notifies the observer when a test case fails.

> **Deprecated**: Use the XCTestObservationCenter class and XCTestObservation protocol instead.

## Declaration

```swift
func testCaseDidFail(_ testRun: XCTestRun!, withDescription description: String!, inFile filePath: String!, atLine lineNumber: Int)
```

```objc
- (void) testCaseDidFail:(XCTestRun *) testRun withDescription:(NSString *) description inFile:(NSString *) filePath atLine:(NSUInteger) lineNumber;
```

## Parameters

- `testRun`: The test run object that calls this method.
- `description`: A string description of the failed test.
- `filePath`: A string that represents a file path to a source code file when the test encounters a failure.
- `lineNumber`: An integer value that represents the line number in the source code file when the test encounters a failure.

## See Also

### Monitoring Test Activity
- [func testCaseDidStart(XCTestRun!)](./testcasedidstart%28_%29.md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](./testcasedidstop%28_%29.md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](./testsuitedidstart%28_%29.md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](./testsuitedidstop%28_%29.md)
  Notifies the observer when a test suite stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testcasedidfail(_:withdescription:infile:atline:))*