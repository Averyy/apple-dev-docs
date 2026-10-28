# XCTAssertThrows

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression throws an `NSException`.

## Declaration

```c
#define XCTAssertThrows(expression, ...)
```

## Discussion

This function generates a failure if `expression` doesn’t throw an exception.

## Parameters

- `expression`: An expression.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Testing for Exceptions
- [XCTAssertThrowsSpecific](./xctassertthrowsspecific.md)
  Asserts that an expression throws a specific `NSException`.
- [XCTAssertThrowsSpecificNamed](./xctassertthrowsspecificnamed.md)
  Asserts that an expression throws a specific NSException with a specific name.
- [XCTAssertNoThrow](./xctassertnothrow.md)
  Asserts that an expression doesn’t throw an `NSException`.
- [XCTAssertNoThrowSpecific](./xctassertnothrowspecific.md)
  Asserts that an expression doesn’t throw a specific `NSException`.
- [XCTAssertNoThrowSpecificNamed](./xctassertnothrowspecificnamed.md)
  Asserts that an expression doesn’t throw a specific `NSException` with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertthrows)*