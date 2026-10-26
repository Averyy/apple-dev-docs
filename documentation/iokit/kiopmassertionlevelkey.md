# kIOPMAssertionLevelKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

The CFDictionary key for assertion level in an assertion info dictionary.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```c
#define kIOPMAssertionLevelKey
```

#### Discussion

The value for this key will be a CFNumber, kCFNumberIntType with value `kIOPMAssertionLevelOff` or `kIOPMAssertionLevelOn`. The level reflects the assertion's level set at creation, or adjusted via IOPMAssertionSetLevel


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopmassertionlevelkey)*