# XCTAssertEqual

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two expressions have the same value.

## Declaration

```c
#define XCTAssertEqual(expression1, expression2, ...)
```

## Mentions

- [Defining Test Cases and Test Methods](./defining-test-cases-and-test-methods.md)

#### Discussion

Generates a failure when `expression1 != expression2`.

## Parameters

- `expression1`: An expression of C scalar type.
- `expression2`: A second expression of C scalar type.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for Equality and Inequality
- [XCTAssertEqualObjects](./xctassertequalobjects.md)
  Asserts that two objects are equal.
- [XCTAssertNotEqual](./xctassertnotequal.md)
  Asserts that two expressions don’t have the same value.
- [XCTAssertNotEqualObjects](./xctassertnotequalobjects.md)
  Asserts that two objects aren’t equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequal)*