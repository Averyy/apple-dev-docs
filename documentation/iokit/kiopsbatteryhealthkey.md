# kIOPSBatteryHealthKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current power source's "health" estimate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.4+

## Declaration

```c
#define kIOPSBatteryHealthKey
```

#### Discussion

- Apple-defined battery power sources will publish this key.
- Use value [`kIOPSGoodValue`](./kiopsgoodvalue.md) to describe a well-performing power source,
- Use [`kIOPSFairValue`](./kiopsfairvalue.md) to describe a functional power source with limited capacity
- And use [`kIOPSPoorValue`](./kiopspoorvalue.md) to describe a power source that's not capable of Providing power.
- For power source creators: Providing this key is OPTIONAL.
- Type CFStringRef


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopsbatteryhealthkey)*