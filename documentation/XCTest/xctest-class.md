# XCTest

**Framework**: Xctest  
**Kind**: class

An abstract base class for creating, managing, and executing tests.

## Declaration

```swift
class XCTest
```

## Mentions

- [Set Up and Tear Down State in Your Tests](set-up-and-tear-down-state-in-your-tests.md)

#### Overview

The [`XCTest`](xctest.md) class provides shared functionality that [`XCTestCase`](xctestcase.md) and [`XCTestSuite`](xctestsuite.md) use for creating, managing, and executing tests. In most cases, you subclass [`XCTestCase`](xctestcase.md) directly when defining tests in your project.

## Topics

### Examining Test Properties
- [var name: String](xctest/name.md)
  The name of the test.
- [var testCaseCount: Int](xctest/testcasecount.md)
  The number of test cases in the test.
- [var testRun: XCTestRun?](xctest/testrun.md)
  The test run object that executes the test.
- [var testRunClass: AnyClass?](xctest/testrunclass.md)
  The test run subclass to instantiate when the test runs, which records the test’s results.
### Setting Up and Tearing Down
- [func setUp(completion: ((any Error)?) -> Void)](xctest/setup(completion:).md)
  Provides an opportunity to reset state asynchronously and handle errors before calling each test method in a test case.
- [func setUpWithError() throws](xctest/setupwitherror.md)
  Provides an opportunity to reset state and to throw errors before calling each test method in a test case.
- [func setUp()](xctest/setup.md)
  Provides an opportunity to reset state before calling each test method in a test case.
- [func tearDown(completion: ((any Error)?) -> Void)](xctest/teardown(completion:).md)
  Provides an opportunity to perform cleanup asynchronously and handle errors after each test method in a test case ends.
- [func tearDownWithError() throws](xctest/teardownwitherror.md)
  Provides an opportunity to perform cleanup and to throw errors after each test method in a test case ends.
- [func tearDown()](xctest/teardown.md)
  Provides an opportunity to perform cleanup after each test method in a test case ends.
### Running Tests
- [func perform(XCTestRun)](xctest/perform(_:).md)
  Executes a specific test.
- [func run()](xctest/run.md)
  Creates a test run instance and starts the test.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [XCTestCase](xctestcase.md)
- [XCTestSuite](xctestsuite.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Defining Test Cases and Test Methods](defining-test-cases-and-test-methods.md)
  Add test cases and test methods to a test target to confirm that your code performs as expected.
- [class XCTestCase](xctestcase.md)
  The primary class for defining test cases, test methods, and performance tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctest)*