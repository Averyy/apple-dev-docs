# testSuiteDidStop(_:)

**Framework**: XCTest  
**Kind**: method  
**Role**: Instance Method

Notifies the observer when a test suite stops.

> **Deprecated**: Use the XCTestObservationCenter class and XCTestObservation protocol instead.

## Declaration

```swift
func testSuiteDidStop(_ testRun: XCTestRun!)
```

```objc
- (void) testSuiteDidStop:(XCTestRun *) testRun;
```

## Parameters

- `testRun`: The test run object calling this method.

## See Also

### Monitoring Test Activity
- [func testCaseDidFail(XCTestRun!, withDescription: String!, inFile: String!, atLine: Int)](./testcasedidfail%28_,withdescription,infile,atline%29.md)
  Notifies the observer when a test case fails.
- [func testCaseDidStart(XCTestRun!)](./testcasedidstart%28_%29.md)
  Notifies the observer when a test case starts.
- [func testCaseDidStop(XCTestRun!)](./testcasedidstop%28_%29.md)
  Notifies the observer when a test case stops.
- [func testSuiteDidStart(XCTestRun!)](./testsuitedidstart%28_%29.md)
  Notifies the observer when a test suite starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestobserver/testsuitedidstop(_:))*