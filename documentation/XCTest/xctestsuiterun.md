# XCTestSuiteRun

**Framework**: XCTest  
**Kind**: class

An object that collects information about a specific execution of a test suite.

## Declaration

```swift
class XCTestSuiteRun
```

#### Overview

The test runner manages the creation and tracking of `XCTestSuiteRun` for an [`XCTestSuite`](xctestsuite.md).

## Topics

### Managing Test Runs
- [func addTestRun(XCTestRun)](xctestsuiterun/addtestrun(_:).md)
  Adds a test run to the test suite.
- [var testRuns: [XCTestRun]](xctestsuiterun/testruns.md)
  An array of test runs that the test suite manages.

## Relationships

### Inherits From
- [XCTestRun](xctestrun.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class XCTestCaseRun](xctestcaserun.md)
  An object that collects information about a specific execution of a test case.
- [class XCTestRun](xctestrun.md)
  A base class for collecting information about a specific execution of a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuiterun)*