# Equality and Inequality Assertions

**Framework**: XCTest  
**Role**: API Collection

Check whether two values are equal or unequal.

## Topics

### Tests for Equality and Inequality
- [func XCTAssertEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertequal%28_,_,_,file,line%29.md)
  Asserts that two values are equal.
- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotequal%28_,_,_,file,line%29.md)
  Asserts that two values are not equal.
- [XCTAssertEqual](./xctassertequal.md)
  Asserts that two expressions have the same value.
- [XCTAssertEqualObjects](./xctassertequalobjects.md)
  Asserts that two objects are equal.
- [XCTAssertNotEqual](./xctassertnotequal.md)
  Asserts that two expressions don’t have the same value.
- [XCTAssertNotEqualObjects](./xctassertnotequalobjects.md)
  Asserts that two objects aren’t equal.
### Tests for Identical Objects
- [func XCTAssertIdentical(@autoclosure () throws -> AnyObject?, @autoclosure () throws -> AnyObject?, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertidentical%28_,_,_,file,line%29.md)
  Asserts that two values are identical.
- [func XCTAssertNotIdentical(@autoclosure () throws -> AnyObject?, @autoclosure () throws -> AnyObject?, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotidentical%28_,_,_,file,line%29.md)
  Asserts that two values aren’t identical.
- [XCTAssertIdentical](./xctassertidentical.md)
  Asserts that two values are identical.
- [XCTAssertNotIdentical](./xctassertnotidentical.md)
  Asserts that two values aren’t identical.
### Tests for Equality Within a Specified Accuracy
- [func XCTAssertEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertequal%28_,_,accuracy,_,file,line%29-6frfw.md)
  Asserts that two floating-point values are equal within a specified accuracy.
- [func XCTAssertEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertequal%28_,_,accuracy,_,file,line%29-4epu5.md)
  Asserts that two numeric values are equal within a specified accuracy.
- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotequal%28_,_,accuracy,_,file,line%29-7jcd6.md)
  Asserts that two floating-point values aren’t equal within a specified accuracy.
- [func XCTAssertNotEqual<T>(@autoclosure () throws -> T, @autoclosure () throws -> T, accuracy: T, @autoclosure () -> String, file: StaticString, line: UInt)](./xctassertnotequal%28_,_,accuracy,_,file,line%29-326vc.md)
  Asserts that two numeric values aren’t equal within a specified accuracy.
- [XCTAssertEqualWithAccuracy](./xctassertequalwithaccuracy.md)
  Asserts that two expressions have the same value within a specified accuracy.
- [XCTAssertNotEqualWithAccuracy](./xctassertnotequalwithaccuracy.md)
  Asserts that two expressions don’t have the same value within a specified accuracy.

## See Also

### Test assertions
- [Boolean Assertions](./boolean-assertions.md)
  Test a condition that generates a true or false result.
- [Nil and Non-Nil Assertions](./nil-and-non-nil-assertions.md)
  Check whether a test condition has, or doesn’t have, a value.
- [Comparable Value Assertions](./comparable-value-assertions.md)
  Compare two values to determine whether one is larger or smaller than the other.
- [Error Assertions](./error-assertions.md)
  Check whether a function call throws, or doesn’t throw, an error.
- [NSException Assertions](./nsexception-assertions.md)
  Check whether a function call throws, or doesn’t throw, an exception.
- [Unconditional Test Failures](./unconditional-test-failures.md)
  Generate a failure immediately and unconditionally.
- [Expected Failures](./expected-failures.md)
  Anticipate known test failures to prevent failing tests from affecting your workflows.
- [Methods for Skipping Tests](./methods-for-skipping-tests.md)
  Skip tests when meeting specified conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/equality-and-inequality-assertions)*