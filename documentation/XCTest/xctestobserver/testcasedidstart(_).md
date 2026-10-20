# testCaseDidStart(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Notifies the observer when a test case starts.

> **Deprecated**: Use the XCTestObservationCenter class and XCTestObservation protocol instead.

## Declaration

```swift
func testCaseDidStart(_ testRun: XCTestRun!)
```

```objc
- (void) testCaseDidStart:(XCTestRun *) testRun;
```

## Parameters

- `testRun`: The test run object that calls this method.

## See Also

### Monitoring Test Activity
- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](./testcasedidfail%28_,withdescription,infile,atline%29.md)
  Notifies the observer when a test case fails.
- [func testCaseDidStop(XCTestRun!)](./testcasedidstop%28_%29.md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](./testsuitedidstart%28_%29.md)
  Notifies the observer when a test suite starts.
- [func testSuiteDidStop(XCTestRun!)](./testsuitedidstop%28_%29.md)
  Notifies the observer when a test suite stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testcasedidstart(_:))*