# XCTAssertNoThrowSpecificNamed

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression doesn’t throw a specific `NSException` with a specific name.

## Declaration

```c
#define XCTAssertNoThrowSpecificNamed(expression, exception_class, exception_name, ...)
```

#### Discussion

This function generates a failure if `expression` throws an [`NSException`](../Foundation/nsexception.md) of class `exception_class` with a name of `exception_name`.

## Parameters

- `expression`: An expression.
- `exception_class`: The class of the exception.
- `exception_name`: The name of the exception.
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
- [XCTAssertNoThrowSpecific](./xctassertnothrowspecific.md)
  Asserts that an expression doesn’t throw a specific `NSException`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnothrowspecificnamed)*