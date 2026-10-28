# kIOPMAssertionTypeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The CFDictionary key for assertion type in an assertion info dictionary.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOPMAssertionTypeKey
```

## Discussion

The value for this key will be a CFStringRef, with the value of the assertion type specified at creation time. Note that macOS may substitute a support assertion type string if the caller specifies a deprecated assertion type; in that case the value for this key could differ from the caller-provided assertion type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertiontypekey)*