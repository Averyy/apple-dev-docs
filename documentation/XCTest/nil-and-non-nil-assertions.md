# Nil and Non-Nil Assertions

**Framework**: Xctest

Check whether a test condition has, or doesn’t have, a value.

## Topics

### Tests for a Nil Condition
- [func XCTAssertNil(@autoclosure () throws -> Any?, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnil(_:_:file:line:).md)
  Asserts that an expression is `nil`.
### Tests for a Non-Nil Condition
- [func XCTAssertNotNil(@autoclosure () throws -> Any?, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertnotnil(_:_:file:line:).md)
  Asserts that an expression is not `nil`.
- [func XCTUnwrap<T>(@autoclosure () throws -> T?, @autoclosure () -> String, file: StaticString, line: UInt) throws -> T](xctunwrap(_:_:file:line:).md)
  Asserts that an expression is not `nil,` and returns the unwrapped value.

## See Also

- [Boolean Assertions](boolean-assertions.md)
  Test a condition that generates a true or false result.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/nil-and-non-nil-assertions)*