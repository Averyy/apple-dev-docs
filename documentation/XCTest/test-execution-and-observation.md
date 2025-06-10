# Test Execution and Observation

**Framework**: XCTest

Observe, introspect, and customize the test execution flow.

## Topics

### Test Failures
- [struct XCTIssue](xctissue-swift.struct.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTIssueReference](xctissuereference.md)
  An object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTMutableIssue](xctmutableissue.md)
  A mutable object that represents a test failure, and includes source code call stacks for test reporting and investigation.
- [class XCTSourceCodeContext](xctsourcecodecontext.md)
  An object that contains call stack and source code location details to provide context for a point of execution in a test.
- [class XCTSourceCodeFrame](xctsourcecodeframe.md)
  An object that represents a single frame in a call stack that supports retrieval of symbol information for the address.
- [class XCTSourceCodeLocation](xctsourcecodelocation.md)
  An object that contains a file URL and line number that represents a distinct location in source code.
- [class XCTSourceCodeSymbolInfo](xctsourcecodesymbolinfo.md)
  An object that contains symbolication information for a specified frame in a call stack.
### Test Runs
- [class XCTestCaseRun](xctestcaserun.md)
  An object that collects information about a specific execution of a test case.
- [class XCTestSuiteRun](xctestsuiterun.md)
  An object that collects information about a specific execution of a test suite.
- [class XCTestRun](xctestrun.md)
  A base class for collecting information about a specific execution of a test.
### Test Observation
- [protocol XCTestObservation](xctestobservation.md)
  A protocol that defines methods the test runner calls in response to significant events during test runs.
- [class XCTestObservationCenter](xctestobservationcenter.md)
  Provides information about the progress of test runs to registered observers.
### Test Suites
- [class XCTestSuite](xctestsuite.md)
  A collection of test cases to manage as a test suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/test-execution-and-observation)*