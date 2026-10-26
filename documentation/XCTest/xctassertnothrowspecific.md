# XCTAssertNoThrowSpecific

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression doesn’t throw a specific `NSException`.

## Declaration

```c
#define XCTAssertNoThrowSpecific(expression, exception_class, ...)
```

#### Discussion

This function generates a failure if `expression` throws an [`NSException`](../Foundation/nsexception.md) of class `exception_class`.

## Parameters

- `expression`: An expression.
- `exception_class`: The class of the exception.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Testing for Exceptions
- [XCTAssertThrows](./xctassertthrows.md)
  Asserts that an expression throws an `NSException`.
- [XCTAssertThrowsSpecific](./xctassertthrowsspecific.md)
  Asserts that an expression throws a specific `NSException`.
- [XCTAssertThrowsSpecificNamed](./xctassertthrowsspecificnamed.md)
  Asserts that an expression throws a specific NSException with a specific name.
- [XCTAssertNoThrow](./xctassertnothrow.md)
  Asserts that an expression doesn’t throw an `NSException`.
- [XCTAssertNoThrowSpecificNamed](./xctassertnothrowspecificnamed.md)
  Asserts that an expression doesn’t throw a specific `NSException` with a specific name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnothrowspecific)*