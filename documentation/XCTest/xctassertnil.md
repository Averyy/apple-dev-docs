# XCTAssertNil

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression is `nil`.

## Declaration

```c
#define XCTAssertNil(expression, ...)
```

#### Discussion

This function generates a failure when `expression != nil`.

## Parameters

- `expression`: An expression of `id` type.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnil)*