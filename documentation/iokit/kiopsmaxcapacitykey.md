# kIOPSMaxCapacityKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's maximum or "Full Charge Capacity"

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSMaxCapacityKey
```

## Discussion

- Apple-defined power sources will publish this key in units of percent. The value is usually 100%.
- The power source's software may specify the units for this key. The units must be consistent for all capacities reported by this power source.
- For power source creators: Providing this key is REQUIRED.
- Type CFNumber kCFNumberIntType (signed integer)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsmaxcapacitykey)*