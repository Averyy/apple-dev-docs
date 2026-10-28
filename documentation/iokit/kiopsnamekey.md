# kIOPSNameKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSNameKey
```

## Discussion

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is REQUIRED.
- Type CFStringRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsnamekey)*