# Boolean Assertions

**Framework**: XCTest

Test a condition that generates a true or false result.

## Topics

### Tests for True Conditions
- [func XCTAssert(@autoclosure () throws -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](xctassert(_:_:file:line:).md)
  Asserts that an expression is true.
- [func XCTAssertTrue(@autoclosure () throws -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](xctasserttrue(_:_:file:line:).md)
  Asserts that an expression is true.
### Tests for False Conditions
- [func XCTAssertFalse(@autoclosure () throws -> Bool, @autoclosure () -> String, file: StaticString, line: UInt)](xctassertfalse(_:_:file:line:).md)
  Asserts that an expression is false.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/boolean-assertions)*