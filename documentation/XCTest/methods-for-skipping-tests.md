# Methods for Skipping Tests

**Framework**: XCTest

Skip tests when meeting specified conditions.

#### Overview

Use `XCTSkipIf()` or `XCTSkipUnless()` when you have a Boolean condition that you can use to evaluate when to skip tests.

In Swift, throw an `XCTSkip` error when you have other circumstances that result in skipped tests. In Objective-C use `XCTSkip`. For example:

## Topics

### Methods for Skipping Tests
- [func XCTSkipIf(@autoclosure () throws -> Bool, @autoclosure () -> String?, file: StaticString, line: UInt) throws](xctskipif(_:_:file:line:).md)
  Skips remaining tests in a test method if the specified condition is met.
- [func XCTSkipUnless(@autoclosure () throws -> Bool, @autoclosure () -> String?, file: StaticString, line: UInt) throws](xctskipunless(_:_:file:line:).md)
  Skips remaining tests in a test method unless the specified condition is met.
- [struct XCTSkip](xctskip-swift.struct.md)
  An error that causes the current test to cease executing and the test runner to mark the test as skipped when the test throws the error.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/methods-for-skipping-tests)*