# Comparable Value Assertions

**Framework**: XCTest

Compare two values to determine whether one is larger or smaller than the other.

## Topics

### Tests for Comparable Values
- [func XCTAssertGreaterThan<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertgreaterthan(_:_:_:file:line:).md)
  Asserts that the value of the first expression is greater than the value of the second expression.
- [func XCTAssertGreaterThanOrEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertgreaterthanorequal(_:_:_:file:line:).md)
  Asserts that the value of the first expression is greater than or equal to the value of the second expression.
- [func XCTAssertLessThanOrEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertlessthanorequal(_:_:_:file:line:).md)
  Asserts that the value of the first expression is less than or equal to the value of the second expression.
- [func XCTAssertLessThan<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertlessthan(_:_:_:file:line:).md)
  Asserts that the value of the first expression is less than the value of the second expression.

## See Also

- [Boolean Assertions](boolean-assertions.md)
  Test a condition that generates a true or false result.
- [Nil and Non-Nil Assertions](nil-and-non-nil-assertions.md)
  Check whether a test condition has, or doesn’t have, a value.
- [Equality and Inequality Assertions](equality-and-inequality-assertions.md)
  Check whether two values are equal or unequal.
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

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/comparable-value-assertions)*