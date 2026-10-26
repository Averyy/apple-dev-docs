# XCTAssertEqualObjects

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two objects are equal.

## Declaration

```c
#define XCTAssertEqualObjects(expression1, expression2, ...)
```

#### Discussion

Generates a failure when `expression1` is not equal to `expression2`.

## Parameters

- `expression1`: An expression of `id` type.
- `expression2`: A second expression of `id` type.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Related Documentation
- [XCTAssertIdentical](./xctassertidentical.md)
  Asserts that two values are identical.
### Tests for Equality and Inequality
- [XCTAssertEqual](./xctassertequal.md)
  Asserts that two expressions have the same value.
- [XCTAssertNotEqual](./xctassertnotequal.md)
  Asserts that two expressions don’t have the same value.
- [XCTAssertNotEqualObjects](./xctassertnotequalobjects.md)
  Asserts that two objects aren’t equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequalobjects)*