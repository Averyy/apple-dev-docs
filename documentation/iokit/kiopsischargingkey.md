# kIOPSIsChargingKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's charging state

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSIsChargingKey
```

#### Discussion

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is REQUIRED.
- Type CFBoolean - kCFBooleanTrue or kCFBooleanFalse


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsischargingkey)*