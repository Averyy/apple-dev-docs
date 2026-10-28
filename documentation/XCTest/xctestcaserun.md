# XCTestCaseRun

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An object that collects information about a specific execution of a test case.

## Declaration

```swift
class XCTestCaseRun
```

```objc
@interface XCTestCaseRun : XCTestRun
```

## Overview

The test runner manages the creation and tracking of `XCTestCaseRun` for each [`XCTestCase`](./xctestcase.md) in an [`XCTestSuite`](./xctestsuite.md).

## Topics

### Deprecated
- [func recordFailure(inTest: XCTestCase, withDescription: String, inFile: String, atLine: Int, expected: Bool)](./xctestcaserun/recordfailure%28intest,withdescription,infile,atline,expected%29.md)
  Records a test failure during test execution for this test run.

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
- [class XCTestSuiteRun](./xctestsuiterun.md)
  An object that collects information about a specific execution of a test suite.
- [class XCTestRun](./xctestrun.md)
  A base class for collecting information about a specific execution of a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcaserun)*