# kIOPSCurrentCapacityKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's capacity.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSCurrentCapacityKey
```

## Discussion

- Apple-defined power sources will publish this key in units of percent.
- The power source's software may specify the units for this key. The units must be consistent for all capacities reported by this power source. The power source will usually define this number in units of percent, or mAh.
- Clients may derive a percentage of power source battery remaining by dividing "Current Capacity" by "Max Capacity"
- For power source creators: Providing this key is REQUIRED.
- Type CFNumber kCFNumberIntType (signed integer)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopscurrentcapacitykey)*