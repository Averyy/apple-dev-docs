# XCTAssertNotEqualObjects

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two objects aren’t equal.

## Declaration

```c
#define XCTAssertNotEqualObjects(expression1, expression2, ...)
```

#### Discussion

Generates a failure when `expression1` is equal to `expression2`.

## Parameters

- `expression1`: An expression of `id` type.
- `expression2`: A second expression of `id` type.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Related Documentation
- [XCTAssertNotIdentical](./xctassertnotidentical.md)
  Asserts that two values aren’t identical.
### Tests for Equality and Inequality
- [XCTAssertEqual](./xctassertequal.md)
  Asserts that two expressions have the same value.
- [XCTAssertEqualObjects](./xctassertequalobjects.md)
  Asserts that two objects are equal.
- [XCTAssertNotEqual](./xctassertnotequal.md)
  Asserts that two expressions don’t have the same value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotequalobjects)*