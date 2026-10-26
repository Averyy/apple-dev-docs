# XCTestSuite

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

A collection of test cases to manage as a test suite.

## Declaration

```swift
class XCTestSuite
```

```objc
@interface XCTestSuite : XCTest
```

#### Overview

Typically, Xcode automatically manages test suites for you. Only use [`XCTestSuite`](./xctestsuite.md) if you need to define your own custom test suites programmatically.

## Topics

### Creating Test Suites
- [class var `default`: XCTestSuite](./xctestsuite/default.md)
  Creates a suite of test suites that represents all test case methods in the current runtime.
- [init(name: String)](./xctestsuite/init%28name%29.md)
  Creates a test suite with the specified name.
- [convenience init(forBundlePath: String)](./xctestsuite/init%28forbundlepath%29.md)
  Creates a test suite with the bundle at the specified path.
- [convenience init(forTestCaseClass: AnyClass)](./xctestsuite/init%28fortestcaseclass%29.md)
  Creates a test suite that contains all test methods in the specified class.
- [convenience init(forTestCaseWithName: String)](./xctestsuite/init%28fortestcasewithname%29.md)
  Creates a test suite that contains a test case with the specified name.
- [+ testSuiteWithName:](./xctestsuite/testsuitewithname_.md)
  Creates a test suite with the specified name.
### Managing Tests
- [func addTest(XCTest)](./xctestsuite/addtest%28_%29.md)
  Adds a test to the test suite.
- [var tests: [XCTest]](./xctestsuite/tests.md)
  All tests currently in the test suite.

## Relationships

### Inherits From
- [XCTest](./xctest-page.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctestsuite)*