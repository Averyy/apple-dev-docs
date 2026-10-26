# kIOPSHealthConfidenceKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for our confidence in the accuracy of our power source's "health" estimate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPSHealthConfidenceKey
```

#### Discussion

- Apple-defined power sources will no longer publish this key.
- Power source creators should not publish this key.
- For power source creators: This key is DEPRECATED, do not implement it.
- Type CFStringRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopshealthconfidencekey)*