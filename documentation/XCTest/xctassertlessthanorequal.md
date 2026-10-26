# XCTAssertLessThanOrEqual

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that the value of the first expression is less than or equal to the value of the second expression.

## Declaration

```c
#define XCTAssertLessThanOrEqual(expression1, expression2, ...)
```

#### Discussion

This function generates a failure when `expression1 > expression2`.

## Parameters

- `expression1`: An expression of C scalar type.
- `expression2`: An expression of C scalar type.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for Comparable Values
- [XCTAssertGreaterThan](./xctassertgreaterthan.md)
  Asserts that the value of the first expression is greater than the value of the second expression.
- [XCTAssertGreaterThanOrEqual](./xctassertgreaterthanorequal.md)
  Asserts that the value of the first expression is greater than or equal to the value of the second expression.
- [XCTAssertLessThan](./xctassertlessthan.md)
  Asserts that the value of the first expression is less than the value of the second expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertlessthanorequal)*