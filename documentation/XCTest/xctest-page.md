# XCTest

**Framework**: XCTest  
**Kind**: class  
**Role**: Class

An abstract base class for creating, managing, and executing tests.

## Declaration

```swift
class XCTest
```

```objc
@interface XCTest : NSObject
```

## Mentions

- [Set Up and Tear Down State in Your Tests](./set-up-and-tear-down-state-in-your-tests.md)

## Overview

The [`XCTest`](./xctest-page.md) class provides shared functionality that [`XCTestCase`](./xctestcase.md) and [`XCTestSuite`](./xctestsuite.md) use for creating, managing, and executing tests. In most cases, you subclass [`XCTestCase`](./xctestcase.md) directly when defining tests in your project.

## Topics

### Examining Test Properties
- [var name: String](./xctest-page/name.md)
  The name of the test.
- [var testCaseCount: Int](./xctest-page/testcasecount.md)
  The number of test cases in the test.
- [var testRun: XCTestRun?](./xctest-page/testrun.md)
  The test run object that executes the test.
- [var testRunClass: AnyClass?](./xctest-page/testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.
### Setting Up and Tearing Down
- [func setUp(completion: ((any Error)?) -> Void)](./xctest-page/setup%28completion%29.md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](./xctest-page/setupwitherror%28%29.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](./xctest-page/setup%28%29.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](./xctest-page/teardown%28completion%29.md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](./xctest-page/teardownwitherror%28%29.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](./xctest-page/teardown%28%29.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.
### Running Tests
- [func perform(XCTestRun)](./xctest-page/perform%28_%29.md)
  Executes a specific test.
- [func run()](./xctest-page/run%28%29.md)
  Creates a test run instance and starts the test.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [XCTestCase](./xctestcase.md)
- [XCTestSuite](./xctestsuite.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Test cases and test methods
- [Defining Test Cases and Test Methods](./defining-test-cases-and-test-methods.md)
  Add test cases and test methods to a test target to confirm that your code performs as expected.
- [class XCTestCase](./xctestcase.md)
  The primary class for defining test cases, test methods, and performance tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest)*