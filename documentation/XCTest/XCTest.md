# XCTest

**Framework**: XCTest  
**Kind**: module

Create and run unit tests, performance tests, and UI tests for your Xcode project.

**Availability**:
- xcode 5.0+

#### Overview

Use the XCTest framework to write unit tests for your Xcode projects that integrate seamlessly with Xcode’s testing workflow.

Tests assert that certain conditions are satisfied during code execution, and record test failures (with optional messages) if those conditions aren’t satisfied. Tests can also measure the performance of blocks of code to check for performance regressions. Use XCTest in combination with [`XCUIAutomation`](https://developer.apple.com/documentation/XCUIAutomation) to interact with an application’s UI and validate user interaction flows. For more information, see [`Recording UI automation for testing`](https://developer.apple.com/documentation/XCUIAutomation/recording-ui-automation-for-testing).

> 💡 **Tip**:  Xcode 16 and later includes Swift Testing, a framework for writing unit tests that takes advantage of the powerful capabilities of the Swift programming language. Consider using Swift Testing for new unit test development and migrating existing tests as described in [`Migrating a test from XCTest`](https://developer.apple.com/documentation/Testing/MigratingFromXCTest). A test target can contain tests using both Swift Testing and XCTest, however don’t mix API from the two frameworks in the same test. Continue to use XCTest for user interface tests and [`Performance Tests`](performance-tests.md).

## Topics

### Test cases and test methods
- [Defining Test Cases and Test Methods](defining-test-cases-and-test-methods.md)
  Add test cases and test methods to a test target to confirm that your code performs as expected.
- [class XCTestCase](xctestcase.md)
  The primary class for defining test cases, test methods, and performance tests.
- [class XCTest](xctest.md)
  An abstract base class for creating, managing, and executing tests.
### Test assertions
- [Boolean Assertions](boolean-assertions.md)
  Test a condition that generates a true or false result.
- [Nil and Non-Nil Assertions](nil-and-non-nil-assertions.md)
  Check whether a test condition has, or doesn’t have, a value.
- [Equality and Inequality Assertions](equality-and-inequality-assertions.md)
  Check whether two values are equal or unequal.
- [Comparable Value Assertions](comparable-value-assertions.md)
  Compare two values to determine whether one is larger or smaller than the other.
- [Error Assertions](error-assertions.md)
  Check whether a function call throws, or doesn’t throw, an error.
- [NSException Assertions](nsexception-assertions.md)
  Check whether a function call throws, or doesn’t throw, an exception.
- [Unconditional Test Failures](unconditional-test-failures.md)
  Generate a failure immediately and unconditionally.
- [Expected Failures](expected-failures.md)
  Anticipate known test failures to prevent failing tests from affecting your workflows.
- [Methods for Skipping Tests](methods-for-skipping-tests.md)
  Skip tests when meeting specified conditions.
### Asynchronous tests
- [Asynchronous Tests and Expectations](asynchronous-tests-and-expectations.md)
  Verify that asynchronous code behaves as expected.
### UI tests
- [XCUIAutomation](../XCUIAutomation/XCUIAutomation.md)
  Replicate sequences of interactions and make sure that your app’s user interface behaves as intended.
### Performance tests
- [Performance Tests](performance-tests.md)
  Gather metrics while running your code, and report a failure if the metrics become significantly worse than a baseline value.
### Activities and attachments
- [Activities and Attachments](activities-and-attachments.md)
  Split long tests into substeps with activities, and attach output data like files and screenshots.
### Test execution
- [Test Execution and Observation](test-execution-and-observation.md)
  Observe, introspect, and customize the test execution flow.
### Deprecated
- [Deprecated Symbols](deprecated-symbols.md)
  These symbols are deprecated and are no longer recommended.
### Variables
- [var XCT_UI_TESTING_AVAILABLE: Int32](xct_ui_testing_available.md)
### Functions
- [func XCTAssertNoThrow<T>(@autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnothrow(_:_:file:line:).md)
  Asserts that an expression doesn’t throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/XCTest)*