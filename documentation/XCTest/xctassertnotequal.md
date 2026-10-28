# XCTAssertNotEqual

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two expressions don’t have the same value.

## Declaration

```c
#define XCTAssertNotEqual(expression1, expression2, ...)
```

## Discussion

Generates a failure when `expression1 == expression2`.

## Parameters

- `expression1`: An expression of C scalar type.
- `expression2`: A second expression of C scalar type.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for Equality and Inequality
- [XCTAssertEqual](./xctassertequal.md)
  Asserts that two expressions have the same value.
- [XCTAssertEqualObjects](./xctassertequalobjects.md)
  Asserts that two objects are equal.
- [XCTAssertNotEqualObjects](./xctassertnotequalobjects.md)
  Asserts that two objects aren’t equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotequal)*