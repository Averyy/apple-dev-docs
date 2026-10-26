# kIOPSMaxErrKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's percentage error in capacity reporting.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPSMaxErrKey
```

#### Discussion

In internal batteries, this refers to the battery pack's estimated percentage error.

- Apple-defined battery power sources will publish this key, but only if it's defined for the battery.
- For power source creators: Providing this key is OPTIONAL.
- Type CFNumberRef kCFNumberIntType, non-negative integer


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsmaxerrkey)*