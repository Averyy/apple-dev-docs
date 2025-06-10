# XCTestCaseRun

**Framework**: XCTest  
**Kind**: class

An object that collects information about a specific execution of a test case.

## Declaration

```swift
class XCTestCaseRun
```

#### Overview

The test runner manages the creation and tracking of `XCTestCaseRun` for each [`XCTestCase`](xctestcase.md) in an [`XCTestSuite`](xctestsuite.md).

## Topics

### Deprecated
- [func recordFailure(inTest: XCTestCase, withDescription: String, inFile: String, atLine: Int, expected: Bool)](xctestcaserun/recordfailure(intest:withdescription:infile:atline:expected:).md)
  Records a test failure during test execution for this test run.

## Relationships

### Inherits From
- [XCTestRun](xctestrun.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class XCTestSuiteRun](xctestsuiterun.md)
  An object that collects information about a specific execution of a test suite.
- [class XCTestRun](xctestrun.md)
  A base class for collecting information about a specific execution of a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestcaserun)*