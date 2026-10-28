# kIOPSIsPresentKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's presence.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSIsPresentKey
```

## Discussion

- Apple-defined power sources will publish this key.
- For instance, a portable with the capacity for two batteries but with only one present would show two power source dictionaries, but kIOPSIsPresentKey would have the value kCFBooleanFalse in one of them.
- For power source creators: Providing this key is REQUIRED.
- Type CFBoolean - kCFBooleanTrue or kCFBooleanFalse


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsispresentkey)*