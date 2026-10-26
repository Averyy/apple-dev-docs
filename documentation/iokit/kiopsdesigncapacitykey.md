# kIOPSDesignCapacityKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's design capacity

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPSDesignCapacityKey
```

#### Discussion

- Apple-defined power sources might not publish this key.
- The power source's software may specify the units for this key. The units must be consistent for all capacities reported by this power source.
- For power source creators: Providing this key is RECOMMENDED.
- Type CFNumber kCFNumberIntType (signed integer)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsdesigncapacitykey)*