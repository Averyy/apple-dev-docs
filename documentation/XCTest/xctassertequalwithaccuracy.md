# XCTAssertEqualWithAccuracy

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two expressions have the same value within a specified accuracy.

## Declaration

```c
#define XCTAssertEqualWithAccuracy(expression1, expression2, accuracy, ...)
```

#### Discussion

Generates a failure when the difference between `expression1` and `expression2` is greater than `accuracy`.

## Parameters

- `expression1`: An expression of C scalar type.
- `expression2`: An expression of C scalar type.
- `accuracy`: An expression of C scalar type describing the maximum difference between `expression1` and `expression2` for these values to be considered equal.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Tests for Equality Within a Specified Accuracy
- [XCTAssertNotEqualWithAccuracy](./xctassertnotequalwithaccuracy.md)
  Asserts that two expressions don’t have the same value within a specified accuracy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertequalwithaccuracy)*