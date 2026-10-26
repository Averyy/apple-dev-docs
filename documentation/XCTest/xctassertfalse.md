# XCTAssertFalse

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression is false.

## Declaration

```c
#define XCTAssertFalse(expression, ...)
```

#### Discussion

This function generates a failure when `expression == true`.

## Parameters

- `expression`: An expression of Boolean type.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertfalse)*