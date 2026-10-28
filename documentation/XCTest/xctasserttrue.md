# XCTAssertTrue

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression is true.

## Declaration

```c
#define XCTAssertTrue(expression, ...)
```

## Discussion

This function generates a failure when `expression == false` and is equivalent to [`XCTAssert`](./xctassert.md).

## Parameters

- `expression`: An expression of Boolean type.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for True Conditions
- [XCTAssert](./xctassert.md)
  Asserts that an expression is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctasserttrue)*