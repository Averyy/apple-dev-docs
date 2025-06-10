# Error Assertions

**Framework**: XCTest

Check whether a function call throws, or doesn’t throw, an error.

## Topics

### Tests for Errors
- [func XCTAssertThrowsError<T>(@autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt, (any Error) -> Void)](xctassertthrowserror(_:_:file:line:_:).md)
  Asserts that an expression throws an error.

## See Also

- [Boolean Assertions](boolean-assertions.md)
  Test a condition that generates a true or false result.
- [Nil and Non-Nil Assertions](nil-and-non-nil-assertions.md)
  Check whether a test condition has, or doesn’t have, a value.
- [Equality and Inequality Assertions](equality-and-inequality-assertions.md)
  Check whether two values are equal or unequal.
- [Comparable Value Assertions](comparable-value-assertions.md)
  Compare two values to determine whether one is larger or smaller than the other.
- [NSException Assertions](nsexception-assertions.md)
  Check whether a function call throws, or doesn’t throw, an exception.
- [Unconditional Test Failures](unconditional-test-failures.md)
  Generate a failure immediately and unconditionally.
- [Expected Failures](expected-failures.md)
  Anticipate known test failures to prevent failing tests from affecting your workflows.
- [Methods for Skipping Tests](methods-for-skipping-tests.md)
  Skip tests when meeting specified conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/error-assertions)*