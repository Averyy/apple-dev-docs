# XCTestSuiteRun

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that collects information about a specific execution of a test suite.

## Declaration

```swift
class XCTestSuiteRun
```

```objc
@interface XCTestSuiteRun : XCTestRun
```

## Overview

The test runner manages the creation and tracking of `XCTestSuiteRun` for an [`XCTestSuite`](./xctestsuite.md).

## Topics

### Managing Test Runs
- [func addTestRun(XCTestRun)](./xctestsuiterun/addtestrun%28_%29.md)
  Adds a test run to the test suite.
- [var testRuns: [XCTestRun]](./xctestsuiterun/testruns.md)
  An array of test runs that the test suite manages.

## Relationships

### Inherits From
- [XCTestRun](./xctestrun.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Test Runs
- [class XCTestCaseRun](./xctestcaserun.md)
  An object that collects information about a specific execution of a test case.
- [class XCTestRun](./xctestrun.md)
  A base class for collecting information about a specific execution of a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuiterun)*