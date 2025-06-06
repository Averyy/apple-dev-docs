# XCTestSuite

**Framework**: Xctest  
**Kind**: class

A collection of test cases to manage as a test suite.

## Declaration

```swift
class XCTestSuite
```

#### Overview

Typically, Xcode automatically manages test suites for you. Only use [`XCTestSuite`](xctestsuite.md) if you need to define your own custom test suites programmatically.

## Topics

### Creating Test Suites
- [class var `default`: XCTestSuite](xctestsuite/default.md)
  Creates a suite of test suites that represents all test case methods in the current runtime.
- [init(name: String)](xctestsuite/init(name:).md)
  Creates a test suite with the specified name.
- [convenience init(forBundlePath: String)](xctestsuite/init(forbundlepath:).md)
  Creates a test suite with the bundle at the specified path.
- [convenience init(forTestCaseClass: AnyClass)](xctestsuite/init(fortestcaseclass:).md)
  Creates a test suite that contains all test methods in the specified class.
- [convenience init(forTestCaseWithName: String)](xctestsuite/init(fortestcasewithname:).md)
  Creates a test suite that contains a test case with the specified name.
### Managing Tests
- [func addTest(XCTest)](xctestsuite/addtest(_:).md)
  Adds a test to the test suite.
- [var tests: [XCTest]](xctestsuite/tests.md)
  All tests currently in the test suite.

## Relationships

### Inherits From
- [XCTest](xctest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite)*