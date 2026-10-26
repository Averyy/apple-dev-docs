# XCTAssertIdentical

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two values are identical.

## Declaration

```c
#define XCTAssertIdentical(expression1, expression2, ...)
```

#### Discussion

Compare two values of type `id`. The values are identical if they’re the same instance.

## Parameters

- `expression1`: An expression of type `id`.
- `expression2`: A second expression of type `id`.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Related Documentation
- [XCTAssertEqualObjects](./xctassertequalobjects.md)
  Asserts that two objects are equal.
### Tests for Identical Objects
- [XCTAssertNotIdentical](./xctassertnotidentical.md)
  Asserts that two values aren’t identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertidentical)*