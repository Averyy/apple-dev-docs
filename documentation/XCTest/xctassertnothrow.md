# XCTAssertNoThrow

**Framework**: XCTest  
**Kind**: macro  
**Role**: Macro

Asserts that an expression doesn’t throw an `NSException`.

## Declaration

```c
#define XCTAssertNoThrow(expression, ...)
```

#### Discussion

This function generates a failure if `expression` throws an exception.

## Parameters

- `expression`: An expression.
- `…`: An optional description of the failure. A literal [`NSString`](../Foundation/nsstring.md), optionally with string format specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xctest/xctassertnothrow)*