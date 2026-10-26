# kIOPSPowerSourceStateKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

CFDictionary key for the current source of power.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```c
#define kIOPSPowerSourceStateKey
```

#### Discussion

- Apple-defined power sources will publish this key.
- For power source creators: Providing this key is REQUIRED.
- [`kIOPSBatteryPowerValue`](./kiopsbatterypowervalue.md) indicates power source is drawing internal power; [`kIOPSACPowerValue`](./kiopsacpowervalue.md) indicates power source is connected to an external power source.
- Type CFString, value is [`kIOPSACPowerValue`](./kiopsacpowervalue.md), [`kIOPSBatteryPowerValue`](./kiopsbatterypowervalue.md), or [`kIOPSOffLineValue`](./kiopsofflinevalue.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiopspowersourcestatekey)*