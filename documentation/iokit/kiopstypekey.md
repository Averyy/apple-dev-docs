# kIOPSTypeKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the type of the power source

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.6+

## Declaration

```c
#define kIOPSTypeKey
```

## Discussion

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is REQUIRED.
- Type CFStringRef. Valid transport types are kIOPSUPSType or kIOPSInternalBatteryType.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopstypekey)*