# XCTAssert

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression is true.

## Declaration

```c
#define XCTAssert(expression, ...)
```

#### Discussion

This function generates a failure when `expression == false` and is equivalent to [`XCTAssertTrue`](./xctasserttrue.md).

## Parameters

- `expression`: An expression of Boolean type.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for True Conditions
- [XCTAssertTrue](./xctasserttrue.md)
  Asserts that an expression is true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassert)*