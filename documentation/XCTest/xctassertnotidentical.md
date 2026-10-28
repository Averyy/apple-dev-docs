# XCTAssertNotIdentical

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that two values aren’t identical.

## Declaration

```c
#define XCTAssertNotIdentical(expression1, expression2, ...)
```

## Discussion

Compare two values of type `id`. The values aren’t identical if they’re not the same instance.

## Parameters

- `expression1`: An expression of type `id`.
- `expression2`: A second expression of type `id`.
- `…`: An optional description of a failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.

## See Also

### Related Documentation
- [XCTAssertNotEqualObjects](./xctassertnotequalobjects.md)
  Asserts that two objects aren’t equal.
### Tests for Identical Objects
- [XCTAssertIdentical](./xctassertidentical.md)
  Asserts that two values are identical.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnotidentical)*